from crewai import Agent
from llm import llm


def create_recommendation_agent():

    return Agent(
        role="Program Recommendation Specialist",

        goal=(
            "Identify programs that fit the student's academic background "
            "and stated interests."
        ),

        backstory=(
            "You help students understand which academic programs align "
            "with their qualifications and interests. You explain the "
            "reasoning behind recommendations."
        ),

        llm=llm,

        verbose=True
    )
