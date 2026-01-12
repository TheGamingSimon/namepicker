from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return {"Hello": "World"}

@router.get("/names")
def names():
    return {"Hello": "World"}

@router.get("/classes")
def classes():
    return {"Hello": "World"}

@router.get("/classes/{id}")
def classes(id: int):
    return {"Hello": "World"}
