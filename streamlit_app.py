import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Get API key from Streamlit secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

## Function to load Gemini model and get response
def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-2.0-flash')
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

## Initialize Streamlit app
st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the image")

if submit:
    response = get_gemini_response(input, image)
    st.subheader("The Response is")
    st.write(response)
