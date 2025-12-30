from fastapi import APIRouter
from app.services.execution_service import run_test
router = APIRouter(prefix="/test")
@router.post("")
def test():
    return run_test()