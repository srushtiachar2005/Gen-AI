from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Research Assistant")
user_input = st.text_input("Enter your query:") 
if st.button("Get Response"):
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    response = model.invoke(user_input)
    st.write(response.content)