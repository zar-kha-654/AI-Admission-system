import streamlit as st
from groq import Groq
from crewai import BaseLLM


client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)


class GroqLLM(BaseLLM):

    def __init__(self, model="openai/gpt-oss-120b", temperature=0.2):
        super().__init__(
            model=model,
            temperature=temperature
        )

    def call(
        self,
        messages,
        tools=None,
        callbacks=None,
        available_functions=None,
        **kwargs
    ):

        # CrewAI may send a simple string
        if isinstance(messages, str):
            messages = [
                {
                    "role": "user",
                    "content": messages
                }
            ]

        # Convert CrewAI messages into normal Groq messages
        groq_messages = []

        for message in messages:
            groq_messages.append(
                {
                    "role": message["role"],
                    "content": message["content"]
                }
            )

        completion = client.chat.completions.create(
            model=self.model,
            messages=groq_messages,
            temperature=self.temperature
        )

        return completion.choices[0].message.content


llm = GroqLLM()
