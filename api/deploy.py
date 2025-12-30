from fastapi import APIRouter
from app.services.clasp_service import deploy

router = APIRouter(prefix="/deploy")

@ router.post("")
def deploy_api():
    return deploy()