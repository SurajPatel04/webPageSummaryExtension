from fastapi import FastAPI, APIRouter

router = APIRouter(
    prefix="/user",
    tags=["users"]
)


@router.get("/")
def test():
    return {"data":"testing"}