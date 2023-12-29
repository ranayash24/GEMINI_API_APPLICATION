
#from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones
model = genai.GenerativeModel('gemini-pro-vision')
def get_gemini_response(input, image):
    if input !="":
         response = model.generate_content([input, image])
    else:
         response= model.generate_content(image)
    return response.text


##initialize our streamlit app

st.set_page_config(page_title="Imgage Demo")

st.header("Gemini LLM Application")
input = st.text_input("Input prompt:" , key = "input")

uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])
image=""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
  
submit = st.button("Tell me about this image")

#if submit is clicked:
if submit:
        
    response = get_gemini_response(input ,image)
    st.header("the response is :")
    st.write(response)
