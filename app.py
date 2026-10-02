import streamlit as st

from crew import run_admission_system


st.set_page_config(
    page_title="Pak Admission AI",
    page_icon="🎓",
    layout="wide"
)


st.title("🎓 Pakistani University Admission AI")

st.write(
    """
    A multi-agent AI system that analyzes a student's academic profile,
    checks program requirements, evaluates eligibility and provides
    program recommendations.
    """
)


st.info(
    "This is an AI admission guidance system, not an official university admission decision."
)


# ------------------------------------------------
# STUDENT INFORMATION
# ------------------------------------------------

st.header("Student Information")

name = st.text_input(
    "Student Name"
)

education = st.selectbox(
    "Current Qualification",
    [
        "Intermediate",
        "ICS",
        "FSc Pre-Engineering",
        "FSc Pre-Medical",
        "I.Com",
        "A-Level"
    ]
)

percentage = st.number_input(
    "Intermediate / Equivalent Percentage",
    min_value=0.0,
    max_value=100.0,
    value=70.0,
    step=0.1
)

math_background = st.selectbox(
    "Mathematics Background",
    [
        "Yes",
        "No",
        "Not Sure"
    ]
)

interests = st.multiselect(
    "Areas of Interest",
    [
        "Computer Science",
        "Software Engineering",
        "Artificial Intelligence",
        "Data Science",
        "Cyber Security",
        "Business",
        "Management"
    ]
)


# ------------------------------------------------
# RUN SYSTEM
# ------------------------------------------------

if st.button(
    "🚀 Analyze Admission Options",
    type="primary"
):

    if not name:
        st.error("Please enter the student's name.")

    elif not interests:
        st.error("Please select at least one area of interest.")

    else:

        student = {
            "name": name,
            "qualification": education,
            "percentage": percentage,
            "mathematics": math_background,
            "interests": interests
        }

        with st.spinner(
            "AI admission team is analyzing the profile..."
        ):

            try:

                result = run_admission_system(student)

                st.success(
                    "Admission analysis completed."
                )

                st.markdown("## 🎓 Admission Report")

                st.markdown(
                    str(result)
                )

            except Exception as e:

                st.error(
                    f"An error occurred: {e}"
                )

                st.info(
                    "Check your GROQ_API_KEY and installed dependencies."
                )
