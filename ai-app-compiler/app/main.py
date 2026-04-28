from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate(req: PromptRequest):
    prompt = req.prompt

    intent = extract_intent(prompt)
    design = design_system(intent)
    schema = generate_schema(design)

    valid, error = validate_schema(schema)

    if not valid:
        schema = repair_schema(schema, error)

    return {
        "intent": intent,
        "design": design,
        "schema": schema,
        "valid": valid
    }