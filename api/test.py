<<<<<<< HEAD
import subprocess
from fastapi import APIRouter

router = APIRouter()

@router.post("/test")
def test():
    result = subprocess.run(
        ["clasp", "push"],
        capture_output=True,
        text=True
    )
    return {
        "stdout": result.stdout,
        "stderr": result.stderr
    }
=======
from fastapi import APIRouter
from services.execution_service import run_test
router = APIRouter(prefix="/test")
@router.post("")
def test():
    return run_test()
>>>>>>> 9ccf4c3b5649425d0074fe8304f4021b0bd1c5ba
