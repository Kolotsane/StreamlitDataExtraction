import streamlit as st
from PIL import Image

# video
video_file = open("Analytics.mp4", "rb").read()
st.video(video_file)

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


