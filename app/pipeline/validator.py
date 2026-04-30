import json

REQUIRED_KEYS = ["ui_schema", "api_schema", "db_schema", "auth_rules"]

def validate_schema(schema_str):
    try:
        data = json.loads(schema_str)
    except Exception as e:
        return False, f"Invalid JSON: {str(e)}"

    # Check required keys
    for key in REQUIRED_KEYS:
        if key not in data:
            return False, f"Missing key: {key}"

    # -------- CROSS-LAYER CHECKS --------

    # 1. API endpoints should exist
    if "endpoints" not in data["api_schema"]:
        return False, "API schema missing endpoints"

    # 2. DB tables should exist
    if "tables" not in data["db_schema"]:
        return False, "DB schema missing tables"

    # 3. Roles consistency
    roles = data["auth_rules"].get("roles", [])
    if not roles:
        return False, "No roles defined"

    return True, "Valid"