from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.app.data.crud import ClassRepository, SchuelerRepository
from src.app.data.db import Database

router = APIRouter()
db = Database()
klasse = ClassRepository(db)
schueler = SchuelerRepository(db)

class ClassCreate(BaseModel):
    name: str

class StudentCreate(BaseModel):
    vorname: str
    nachname: str
    class_id: int | None = None


class StudentUpdate(BaseModel):
    vorname: str
    nachname: str
    class_id: int | None = None

# Klassen
@router.get("/classes")
def get_classes():
    class_names = klasse.get_classes()
    return {"classes": class_names}

@router.post("/classes")
def create_class(data: ClassCreate):
    new_class = klasse.create_class(data.name)
    return {
        "id": new_class[0],
        "name": new_class[1]
    }

# Schüler
@router.get("/students/{class_id}")
def get_students(class_id: int):
    students = schueler.get_all_names(class_id)
    return {"students": students}

@router.post("/students")
def create_student(data: StudentCreate):
    try:
        created = schueler.create_student(data.vorname, data.nachname, data.class_id)
        return {"id": created[0], "vorname": created[1], "nachname": created[2], "class_id": created[3]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/students/{student_id}")
def update_student(student_id: int, data: StudentUpdate):
    try:
        updated = schueler.update_student(student_id, data.vorname, data.nachname, data.class_id)
        if updated is None:
            raise HTTPException(status_code=404, detail="student not found")
        return {"id": updated[0], "vorname": updated[1], "nachname": updated[2], "class_id": updated[3]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/students/{student_id}")
def delete_student(student_id: int):
    try:
        ok = schueler.delete_student(student_id)
        if not ok:
            raise HTTPException(status_code=404, detail="student not found")
        return {"deleted": True}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Name ziehen
@router.post("/classes/{id}/pick")
def pick_names(id: int, count: int):
    if count <= 0:
        return {"students": []}

    assigned = schueler.pick_and_assign_students(id, count)

    return {
        "students": [
            {
                "id": s[0],
                "vorname": s[1],
                "nachname": s[2],
                "class_id": s[3],
            }
            for s in assigned
        ]
    }

