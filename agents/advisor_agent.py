from crewai import Agent
from llm import llm


def create_advisor_agent():

    return Agent(
        role="University Admission Advisor",

        goal=(
            "Produce a clear final admission report combining profile, "
            "requirements, eligibility and program recommendations."
        ),

        backstory=(
            "You are an experienced academic advisor who communicates "
            "complex admission information in a simple way."
        ),

        llm=llm,

        verbose=True
    )
