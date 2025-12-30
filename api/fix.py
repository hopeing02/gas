from fastapi import APIRouter
from app.core.claude_client import fix_code
from app.core.gas_policy import validate

router = APIRouter(prefix="/fix")
@router.post("")
def fix(payload: dict):
    fixed = fix_code(payload)
    if not validate(fixed):
        return {"error": "Policy violation"}
    return {"code": fixed}
