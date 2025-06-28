import streamlit as st
from model import run_prompt


# Streamlit app to interact with the Gemini model
st.set_page_config(page_title="Prompt Engineering App", layout="centered")
st.title("Prompt Engineering with Gemini")

# prompt types dropbox
prompt_types=[
    "Zero-Shot",
    "Few-Shot",
    "Instruction-Based",
    "Chain-of-Thought",
    "Role-based"
]

selected_prompt = st.selectbox("Choose Prompt Type:",prompt_types)
user_input = st.text_area("Enter your input text here:")


if st.button("Generate Response"):
    with st.spinner("Generating response..."):
        output= run_prompt(selected_prompt, user_input)
        st.markdown("### Generated Response:")
        st.code(output)

