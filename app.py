
import streamlit as st
from llm import generate_response

st.set_page_config(
    page_title="Prompt Engineering LLM",
    page_icon="🤖",
    layout="centered"
)

st.title("Prompt Engineering LLM")
st.write("Generate AI responses using different prompt engineering techniques.")

st.sidebar.header("Settings")

template_name = st.sidebar.selectbox(
    "Choose a Prompt Template",
    [
        "General Question",
        "Summarization",
        "Explain Simply",
        "Creative Writing",
        "Code Assistant"
    ]
)

st.subheader("Enter Your Input")

user_input = st.text_area(
    "Type your question or text here:",
    height=180,
    placeholder="Example: Explain Artificial Intelligence in simple words."
)

if st.button("Generate Response", type="primary"):
    if user_input.strip():
        with st.spinner("Generating response..."):
            result = generate_response(
                user_input,
                template_name
            )

        st.subheader("Generated Response")
        st.write(result)

    else:
        st.warning("Please enter some text before generating a response.")

st.divider()

st.caption("Built using Python, Streamlit, Gemini API, and Prompt Engineering.")

