import json
from fastapi import FastAPI
from pydantic import BaseModel

from app.pipeline.intent import extract_intent
from app.pipeline.design import design_system
from app.pipeline.schema import generate_schema
from app.pipeline.validator import validate_schema
from app.pipeline.repair import repair_schema

from app.utils.metrics import metrics

#  CREATE app FIRST
app = FastAPI()

#  Request model
class PromptRequest(BaseModel):
    prompt: str

#  Home route
@app.get("/")
def home():
    return {"message": "AI App Compiler running 🚀"}

#  Main endpoint
@app.post("/generate")
def generate(req: PromptRequest):
    # count request
    metrics["total_requests"] += 1

    prompt = req.prompt

    intent = extract_intent(prompt)
    design = design_system(intent)
    schema = generate_schema(design)

    valid, error = validate_schema(schema)

    if valid:
        metrics["valid_outputs"] += 1
    else:
        metrics["invalid_outputs"] += 1
        metrics["repairs_triggered"] += 1
        schema = repair_schema(schema, error)

    return {
        "intent": json.loads(intent),
        "design": json.loads(design),
        "schema": json.loads(schema),
        "valid": valid
    }

# NEW: Metrics endpoint
@app.get("/metrics")
def get_metrics():
    return metrics