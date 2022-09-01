import streamlit as st
from PIL import Image

img = Image.open("DS.JPG")
st.image(img, width=1000,)

with st.sidebar:
    # images
    img = Image.open("logo.png")
    st.image(img, width=300)

    # Text/Title
    st.write("🏛 Home")
    st.write("📰 About")
    st.write("🧰 Services")
    st.write("📞✉ Contacts")
    st.write("🔒 Logout")

