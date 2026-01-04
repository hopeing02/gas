from fastapi import APIRouter, HTTPException
from services.clasp_service import clasp_push, clasp_run_test

router = APIRouter()

@router.post("/test")
def test_gas():
    try:
        clasp_push()
        result = clasp_run_test()

        if result == "OK":
            return {
                "status": "success",
                "result": result
            }

        return {
            "status": "fail",
            "result": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
