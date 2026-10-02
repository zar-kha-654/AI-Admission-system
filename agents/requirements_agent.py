from crewai import Agent
from llm import llm


def create_requirements_agent():

    return Agent(
        role="Admission Requirements Analyst",

        goal=(
            "Compare the student's academic profile against the "
            "provided program requirements without inventing requirements."
        ),

        backstory=(
            "You analyze admission requirements using only the supplied "
            "structured program data. You never invent university policies."
        ),

        llm=llm,

        verbose=True
    )
