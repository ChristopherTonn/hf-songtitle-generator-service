from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def healthcheck():
    return {"status": "ok"}