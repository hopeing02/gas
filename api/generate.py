from fastapi import APIRouter
from pydantic import BaseModel
from core.claude_client import generate_code

router = APIRouter()

class GenerateRequest(BaseModel):
    spec: Any

@router.post("/generate")
def generate(req: GenerateRequest):
    code = generate_code(req.spec)
    return {"code": code}
