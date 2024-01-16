from dotenv import load_dotenv
load_dotenv() #loading all environment variables

import streamlit as st
import os
import google.generativeai as genai   
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini  and Gemini pro model to get responses

model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

model_vision = genai.GenerativeModel("gemini-pro-vision")
def get_gemini_vision_response(input,image):
    if input!="":
        response=model_vision.generate_content([input,image])
    else: 
        response=model_vision.generate_content(image)
    return response.text


st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Pro Text LLM Application")
input=st.text_input("Input:",key="input")
submit=st.button("Ask the question")

# When submit is clicked
if submit:
    response=get_gemini_response(input)
    st.subheader("The respose is")
    st.write(response)


st.header('Gemini Pro Vision LLM Application')
input_vision = st.text_input("Input_Prompt: ",key="inputvision")
uploaded_file = st.file_uploader("Choose an image..",type=["jpg","jpeg","png","gif"])
image=""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit_vision = st.button('Tell me about the image')
#if submit is clicked
if submit_vision:
    response=get_gemini_vision_response(input_vision,image)
    st.subheader("The response is")
    st.write(response)


    
     

