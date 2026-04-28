from app.utils.llm import generate_json

def extract_intent(prompt: str):
    return generate_json(f"""
    Extract structured intent from this prompt.

    Return JSON with:
    - features (list)
    - roles (list)
    - entities (list)
    - constraints (list)

    Prompt:
    {prompt}
    """)