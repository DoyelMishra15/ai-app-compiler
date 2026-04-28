# app/utils/llm.py

import json

def generate_json(prompt):
    prompt_lower = prompt.lower()

    features = []
    roles = []
    entities = []

    if "login" in prompt_lower:
        features.append("login")
        entities.append("user")

    if "dashboard" in prompt_lower:
        features.append("dashboard")

    if "admin" in prompt_lower:
        roles.append("admin")

    if "user" in prompt_lower:
        roles.append("user")

    if "payment" in prompt_lower or "premium" in prompt_lower:
        features.append("payment")
        entities.append("subscription")

    return json.dumps({
        "features": list(set(features)) or ["basic_app"],
        "roles": list(set(roles)) or ["user"],
        "entities": list(set(entities)) or ["entity"],
        "constraints": []
    })