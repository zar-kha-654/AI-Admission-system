from crewai import Agent
from llm import llm


def create_profile_agent():

    return Agent(
        role="Student Profile Analyst",

        goal=(
            "Convert the student's educational information into a "
            "clear structured academic profile."
        ),

        backstory=(
            "You specialize in understanding the Pakistani education "
            "system including Matric, Intermediate, ICS, FSc, I.Com, "
            "A-Levels and undergraduate admissions."
        ),

        llm=llm,

        verbose=True
    )
