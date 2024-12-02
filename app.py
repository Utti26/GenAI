import streamlit as st
from PIL import Image
import os

# Load models (implement these based on your notebooks)
from texttoimagegenerator import generate_image_from_text
from imagetotextgenerator import generate_text_from_image
from multilingualtexttoimagegenerator import generate_image_multilingual

st.title("Unified AI Model Interface")

# Sidebar
st.sidebar.title("Navigation")
option = st.sidebar.radio(
    "Choose a model to use:",
    ("Text to Image", "Image to Text", "Multilingual Text to Image")
)

# Text to Image Generator
if option == "Text to Image":
    st.header("Text to Image Generator")
    user_input = st.text_input("Enter a description:")
    if st.button("Generate Image"):
        if user_input:
            image = generate_image_from_text(user_input)
            st.image(image, caption="Generated Image")
        else:
            st.warning("Please enter a description.")

# Image to Text Generator
elif option == "Image to Text":
    st.header("Image to Text Generator")
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        if st.button("Generate Text"):
            description = generate_text_from_image(image)
            st.text_area("Generated Description:", value=description, height=200)

# Multilingual Text to Image Generator
elif option == "Multilingual Text to Image":
    st.header("Multilingual Text to Image Generator")
    user_input = st.text_input("Enter a description (any language):")
    if st.button("Generate Image"):
        if user_input:
            image = generate_image_multilingual(user_input)
            st.image(image, caption="Generated Image")
        else:
            st.warning("Please enter a description.")


