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
