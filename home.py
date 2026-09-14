import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


st.title("Welcome!")

name= st.text_input("What's your name")

age= st.number_input("What's your age?", min_value=0)

if st.button("Say hi"):
    st.write(f"Hello,{name}, I understand you are {age} years old.")

    
client = OpenAI()

response = client.responses.create(
    model="gpt-4o",
    input="Write a one-sentence bedtime story about a unicorn.",
)

st.write(response.output_text)





