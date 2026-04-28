from app.utils.llm import generate_json

def design_system(intent_json: str):
    return generate_json(f"""
    Convert this into system design.

    Include:
    - architecture
    - modules
    - user_flows

    Intent:
    {intent_json}
    """)