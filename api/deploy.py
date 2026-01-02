from fastapi import APIRouter
from services.clasp_service import deploy

router = APIRouter()

@ router.post("/deploy")
def deploy():
    return {"status":"deploy ok"}