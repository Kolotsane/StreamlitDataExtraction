import base64
from cProfile import label

import streamlit as st
from PIL import Image

# images
img = Image.open("logo.png")
st.image(img, width=300, caption="Logo")

# Text/Title
st.title("Document Processing Center")

# files
uploaded_files = st.file_uploader("Choose a pdf invoice file", accept_multiple_files=True)


# adding background


@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_png_as_page_bg(jpg_file):
    bin_str = get_base64_of_bin_file(jpg_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/jpg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return


set_png_as_page_bg('bc.jpg')
