from fastapi import APIRouter
from core.claude_client import generate_code
router = APIRouter(prefix="/generate")
@router.post("")
def generate(spec: dict):
    return {"code": generate_code(spec)}