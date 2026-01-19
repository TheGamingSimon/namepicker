from fastapi import APIRouter
from src.app.data.crud import ClassRepository
from src.app.data.db import Database

router = APIRouter()
db = Database()
klasse = ClassRepository(db)
# Klassen
@router.get("/classes")
def get_classes():
    class_names = klasse.get_classes()
    return {"classes": class_names}

@router.get("/classes/{id}")
def get_class(id: int):
    return {"class": {"id": id, "name": "Dummy"}} 

@router.post("/classes")
def create_class():
    return {"message": "Class created"}

@router.put("/classes/{id}")
def update_class(id: int):
    return {"message": f"Class {id} updated"}

@router.delete("/classes/{id}")
def delete_class(id: int):
    return {"message": f"Class {id} deleted"}

# Schüler
@router.get("/students")
def get_students():
    return {"students": []}

@router.get("/students/{id}")
def get_student(id: int):
    return {"student": {"id": id, "name": "Dummy"}} 

@router.post("/students")
def create_student():
    return {"message": "Student created"}

@router.put("/students/{id}")
def update_student(id: int):
    return {"message": f"Student {id} updated"}

@router.delete("/students/{id}")
def delete_student(id: int):
    return {"message": f"Student {id} deleted"}

# Name ziehen
@router.post("/classes/{id}/pick")
def pick_names(id: int, count: int):
    return {"names": [f"Student {i+1}" for i in range(count)]}
