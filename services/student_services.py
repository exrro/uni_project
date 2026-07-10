from fastapi import HTTPException

from data.storage import STUDENTS_FILE, COURSES_FILE, load_data, save_data
from models.student import Student


def _find_student_index(students: list[dict], student_number: str) -> int:
    for index, student in enumerate(students):
        if student["student_number"] == student_number:
            return index
    return -1


def get_all_students() -> list[dict]:
    return load_data(STUDENTS_FILE)


def get_student_by_number(student_number: str) -> dict:
    students = load_data(STUDENTS_FILE)
    for student in students:
        if student["student_number"] == student_number:
            return student
    raise HTTPException(status_code=404, detail="Student not found")


def create_student(
    national_id: str,
    first_name: str,
    last_name: str,
    student_number: str,
    major: str,
) -> dict:
    students = load_data(STUDENTS_FILE)

    for student in students:
        if student["student_number"] == student_number:
            raise HTTPException(status_code=400, detail="Student already exists")
        if student["national_id"] == national_id:
            raise HTTPException(status_code=400, detail="National ID already exists")

    new_student = Student(
        national_id=national_id,
        first_name=first_name,
        last_name=last_name,
        student_number=student_number,
        major=major,
    )

    students.append(new_student.to_dict())
    save_data(STUDENTS_FILE, students)
    return new_student.to_dict()


def update_student(student_number: str, update_data: dict) -> dict:
    students = load_data(STUDENTS_FILE)
    student_index = _find_student_index(students, student_number)

    if student_index == -1:
        raise HTTPException(status_code=404, detail="Student not found")

    current_student = students[student_index]

    new_national_id = update_data.get("national_id", current_student["national_id"])
    if new_national_id != current_student["national_id"]:
        for student in students:
            if student["national_id"] == new_national_id:
                raise HTTPException(status_code=400, detail="National ID already exists")

    current_student["national_id"] = new_national_id
    current_student["first_name"] = update_data.get("first_name", current_student["first_name"])
    current_student["last_name"] = update_data.get("last_name", current_student["last_name"])
    current_student["major"] = update_data.get("major", current_student["major"])
    current_student["full_name"] = f"{current_student['first_name']} {current_student['last_name']}"

    students[student_index] = current_student
    save_data(STUDENTS_FILE, students)
    return current_student


def delete_student(student_number: str) -> dict:
    students = load_data(STUDENTS_FILE)
    courses = load_data(COURSES_FILE)

    student_index = _find_student_index(students, student_number)
    if student_index == -1:
        raise HTTPException(status_code=404, detail="Student not found")

    student = students[student_index]

    for course in courses:
        if student_number in course["students"]:
            course["students"].remove(student_number)

    save_data(COURSES_FILE, courses)

    deleted_student = students.pop(student_index)
    save_data(STUDENTS_FILE, students)

    return {
        "message": "Student deleted successfully",
        "student": deleted_student,
    }
