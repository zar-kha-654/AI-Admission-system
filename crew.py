from crewai import Crew, Task, Process

from agents import (
    create_profile_agent,
    create_requirements_agent,
    create_eligibility_agent,
    create_recommendation_agent,
    create_advisor_agent
)

from data.programs import PROGRAMS


def run_admission_system(student):

    profile_agent = create_profile_agent()
    requirements_agent = create_requirements_agent()
    eligibility_agent = create_eligibility_agent()
    recommendation_agent = create_recommendation_agent()
    advisor_agent = create_advisor_agent()

    # ------------------------------------------------
    # TASK 1
    # ------------------------------------------------

    profile_task = Task(
        description=f"""
        Analyze this student's information:

        {student}

        Create a structured academic profile containing:

        - Education level
        - Academic background
        - Percentage
        - Mathematics status
        - Interests
        - Relevant strengths
        - Missing information

        Do not invent information.
        """,

        expected_output="A structured student academic profile.",

        agent=profile_agent
    )

    # ------------------------------------------------
    # TASK 2
    # ------------------------------------------------

    requirements_task = Task(
        description=f"""
        Using the student's profile from the previous task, compare
        the student against these program requirements:

        {PROGRAMS}

        Identify which requirements are satisfied,
        which are not satisfied,
        and which require verification.

        IMPORTANT:

        Only use the supplied program data.
        Do not invent university requirements.

        GRE and GMAT should not be introduced as undergraduate
        requirements in this Pakistani admissions MVP.
        """,

        expected_output="A detailed requirements comparison.",

        agent=requirements_agent,

        context=[profile_task]
    )

    # ------------------------------------------------
    # TASK 3
    # ------------------------------------------------

    eligibility_task = Task(
        description="""
        Evaluate the requirements analysis.

        For every program classify the student as:

        1. Eligible
        2. Conditionally Eligible
        3. Not Eligible

        Explain the reason for each classification.

        Do not invent missing academic information.
        """,

        expected_output="Eligibility assessment for each program.",

        agent=eligibility_agent,

        context=[
            profile_task,
            requirements_task
        ]
    )

    # ------------------------------------------------
    # TASK 4
    # ------------------------------------------------

    recommendation_task = Task(
        description=f"""
        Based on the student's profile and eligibility results,
        identify the most relevant programs from this catalog:

        {PROGRAMS}

        Consider:

        - Academic background
        - Mathematics
        - Student interests
        - Eligibility
        - Program field

        Give explanations for each recommendation.

        Do not recommend programs that are clearly not eligible.
        """,

        expected_output="A list of suitable programs with explanations.",

        agent=recommendation_agent,

        context=[
            profile_task,
            eligibility_task
        ]
    )

    # ------------------------------------------------
    # TASK 5
    # ------------------------------------------------

    advisor_task = Task(
        description="""
        Create the final student admission report.

        The report should contain:

        ## Student Profile

        ## Requirements Analysis

        ## Eligibility

        ## Recommended Programs

        ## Missing Information

        ## Next Steps

        Make the report easy for a Pakistani student to understand.

        Clearly distinguish between:

        - confirmed information from the supplied dataset
        - AI-generated explanations
        - requirements that need university verification

        Do not claim that this report is an official admission decision.
        """,

        expected_output="A complete admission guidance report.",

        agent=advisor_agent,

        context=[
            profile_task,
            requirements_task,
            eligibility_task,
            recommendation_task
        ]
    )

    # ------------------------------------------------
    # CREW
    # ------------------------------------------------

    crew = Crew(
        agents=[
            profile_agent,
            requirements_agent,
            eligibility_agent,
            recommendation_agent,
            advisor_agent
        ],

        tasks=[
            profile_task,
            requirements_task,
            eligibility_task,
            recommendation_task,
            advisor_task
        ],

        process=Process.sequential,

        verbose=True
    )

    result = crew.kickoff()

    return result
