from fastapi import APIRouter

from schemas.professor_schema import ProfessorCreate, ProfessorUpdate
from services.professor_services import (
    create_professor,
    delete_professor,
    get_all_professors,
    get_professor_by_code,
    update_professor,
)

router = APIRouter(prefix="/professors", tags=["Professors"])


@router.get("/")
def read_professors():
    return get_all_professors()


@router.get("/{professor_code}")
def read_professor(professor_code: str):
    return get_professor_by_code(professor_code)


@router.post("/")
def add_professor(professor: ProfessorCreate):
    return create_professor(
        national_id=professor.national_id,
        first_name=professor.first_name,
        last_name=professor.last_name,
        professor_code=professor.professor_code,
        department=professor.department,
    )


@router.put("/{professor_code}")
def edit_professor(professor_code: str, professor: ProfessorUpdate):
    return update_professor(professor_code, professor.model_dump(exclude_unset=True))


@router.delete("/{professor_code}")
def remove_professor(professor_code: str):
    return delete_professor(professor_code)
