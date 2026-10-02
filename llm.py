import streamlit as st
from crewai import LLM

llm = LLM(
    model="groq/openai/gpt-oss-120b",
    api_key=st.secrets["GROQ_API_KEY"],
)
