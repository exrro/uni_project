from fastapi import APIRouter

from schemas.student_schema import StudentCreate, StudentUpdate
from services.student_services import (
    create_student,
    delete_student,
    get_all_students,
    get_student_by_number,
    update_student,
)


router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/")
def read_students():
    return get_all_students()


@router.get("/{student_number}")
def read_student(student_number: str):
    return get_student_by_number(student_number)


@router.post("/")
def add_student(student: StudentCreate):
    return create_student(
        national_id=student.national_id,
        first_name=student.first_name,
        last_name=student.last_name,
        student_number=student.student_number,
        major=student.major,
    )


@router.put("/{student_number}")
def edit_student(student_number: str, student: StudentUpdate):
    return update_student(student_number, student.model_dump(exclude_unset=True))


@router.delete("/{student_number}")
def remove_student(student_number: str):
    return delete_student(student_number)
