PROMPT_TEMPLATES = {
    "General Question": """
    Answer the following question clearly and accurately:
    {user_input}
    """,

    "Summarization": """
    Summarize the following text in simple English:
    {user_input}
    """,

    "Explain Simply": """
    Explain the following topic in simple words with examples:
    {user_input}
    """,

    "Creative Writing": """
    Write a creative response to the following request:
    {user_input}
    """,

    "Code Assistant": """
    Answer the programming question and provide code if needed:
    {user_input}
    """
}


def get_prompt(template_name, user_input):
    template = PROMPT_TEMPLATES.get(
        template_name,
        PROMPT_TEMPLATES["General Question"]
    )

    return template.format(user_input=user_input)