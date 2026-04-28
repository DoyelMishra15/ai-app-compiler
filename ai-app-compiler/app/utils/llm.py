import json

def generate_json(prompt):
    prompt_lower = prompt.lower()

    # ---------------- INTENT ----------------
    if "extract structured intent" in prompt_lower:
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

        if "payment" in prompt_lower or "premium" in prompt_lower:
            features.append("payment")
            entities.append("subscription")

        return json.dumps({
            "features": features or ["basic_app"],
            "roles": roles or ["user"],
            "entities": entities or ["entity"],
            "constraints": []
        })

    # ---------------- DESIGN ----------------
    elif "system design" in prompt_lower:
        return json.dumps({
            "architecture": "3-tier",
            "modules": ["auth", "payments", "dashboard"],
            "user_flows": [
                "user -> login -> dashboard",
                "user -> subscribe -> payment -> access premium"
            ]
        })

    # ---------------- SCHEMA ----------------
    elif "application schema" in prompt_lower:
        return json.dumps({
            "ui_schema": {
                "pages": ["login", "dashboard"],
                "components": ["form", "table"]
            },
            "api_schema": {
                "endpoints": [
                    {"path": "/login", "method": "POST"},
                    {"path": "/subscribe", "method": "POST"}
                ]
            },
            "db_schema": {
                "tables": [
                    {"name": "users", "fields": ["id", "email", "password"]},
                    {"name": "subscriptions", "fields": ["id", "user_id", "status"]}
                ]
            },
            "auth_rules": {
                "roles": ["user"],
                "permissions": ["access_dashboard", "make_payment"]
            }
        })

    return json.dumps({"error": "unknown stage"})