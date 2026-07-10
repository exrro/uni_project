from fastapi import APIRouter, Body
from services.selection_services import (
    drop_course,
    select_course,
    get_students_by_course,
    update_student_grade
)

router = APIRouter(prefix="/selections", tags=["Selections"])

@router.post("/{student_number}/{course_code}")
def add_selection(student_number: str, course_code: str):
    return select_course(student_number, course_code)

@router.delete("/{student_number}/{course_code}")
def remove_selection(student_number: str, course_code: str):
    return drop_course(student_number, course_code)

# دریافت لیست دانشجویان یک درس خاص
@router.get("/course/{course_code}")
def list_students_in_course(course_code: str):
    return get_students_by_course(course_code)

# ثبت یا ویرایش نمره دانشجو
@router.put("/grade")
def save_grade(data: dict = Body(...)):
    student_number = data.get("student_number")
    course_code = data.get("course_code")
    grade = data.get("grade")

    if not all([student_number, course_code, grade is not None]):
        return {"message": "اطلاعات ناقص است"}

    return update_student_grade(student_number, course_code, float(grade))
