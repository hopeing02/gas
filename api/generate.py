from fastapi import APIRouter
from pydantic import BaseModel
from core.claude_client import generate_code

router = APIRouter()

class GenerateRequest(BaseModel):
    spec: str   # ✅ dict → str 로 변경

@router.post("/generate")
def generate(req: GenerateRequest):
    try:
        code = generate_code(req.spec)
        return {"code": code}
    except Exception as e:
        # 🔥 에러를 그대로 반환
        raise HTTPException(status_code=500, detail=str(e))
