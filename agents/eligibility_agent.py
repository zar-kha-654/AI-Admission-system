from crewai import Agent
from llm import llm


def create_eligibility_agent():

    return Agent(
        role="Eligibility Evaluator",

        goal=(
            "Determine whether the student is eligible, conditionally "
            "eligible, or not eligible for the available programs."
        ),

        backstory=(
            "You carefully evaluate academic qualifications, percentages, "
            "subject requirements and admission tests."
        ),

        llm=llm,

        verbose=True
    )
