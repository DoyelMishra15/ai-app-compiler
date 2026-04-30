from app.utils.llm import generate_json

def generate_schema(design_json: str):
    return generate_json(f"""
    Generate application schema.

    Include:
    - ui_schema (pages, components)
    - api_schema (endpoints, methods)
    - db_schema (tables, fields)
    - auth_rules (roles, permissions)

    Design:
    {design_json}
    """)