from fastapi import FastAPI
from app.pipeline.intent import extract_intent
from app.pipeline.design import design_system
from app.pipeline.schema import generate_schema
from app.pipeline.validator import validate_schema
from app.pipeline.repair import repair_schema

app = FastAPI()

@app.post("/generate")
def generate(prompt: str):
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