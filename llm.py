import streamlit as st
from groq import Groq


client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)


class GroqLLM:
    def __init__(self, model="openai/gpt-oss-120b"):
        self.model = model

    def call(self, prompt):
        completion = client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        return completion.choices[0].message.content


llm = GroqLLM()
