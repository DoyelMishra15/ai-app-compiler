import json

def repair_schema(schema_str, error_msg):
    try:
        data = json.loads(schema_str)
    except:
        data = {}

    # Fix missing keys intelligently
    data.setdefault("ui_schema", {"pages": [], "components": []})
    data.setdefault("api_schema", {"endpoints": []})
    data.setdefault("db_schema", {"tables": []})
    data.setdefault("auth_rules", {"roles": ["user"], "permissions": []})

    # Fix deeper issues
    if "endpoints" not in data["api_schema"]:
        data["api_schema"]["endpoints"] = []

    if "tables" not in data["db_schema"]:
        data["db_schema"]["tables"] = []

    if not data["auth_rules"].get("roles"):
        data["auth_rules"]["roles"] = ["user"]

    return json.dumps(data)