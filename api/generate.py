from fastapi import APIRouter
from pydantic import BaseModel
from core.claude_client import generate_code

router = APIRouter(
    tags=["generate"]
)

class GenerateRequest(BaseModel):
    spec: str   # ✅ dict → str 로 변경

@router.post("/generate")
def generate(req: GenerateRequest):
    code = generate_code(req.spec)
    return {"code": code}
