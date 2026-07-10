from fastapi import HTTPException
from data.storage import STUDENTS_FILE, COURSES_FILE, load_data, save_data

def select_course(student_number: str, course_code: str) -> dict:
    students = load_data(STUDENTS_FILE)
    courses = load_data(COURSES_FILE)
    student = next((s for s in students if s["student_number"] == student_number), None)
    course = next((c for c in courses if c["course_code"] == course_code), None)

    if not student or not course: raise HTTPException(status_code=404, detail="Not found")

    if course_code not in student.setdefault("selected_courses", []):
        student["selected_courses"].append(course_code)
    if student_number not in course.setdefault("students", []):
        course["students"].append(student_number)

    save_data(STUDENTS_FILE, students)
    save_data(COURSES_FILE, courses)
    return {"message": "Success"}

def drop_course(student_number: str, course_code: str) -> dict:
    students = load_data(STUDENTS_FILE)
    courses = load_data(COURSES_FILE)
    student = next((s for s in students if s["student_number"] == student_number), None)
    course = next((c for c in courses if c["course_code"] == course_code), None)

    if student and course:
        if course_code in student.get("selected_courses", []):
            student["selected_courses"].remove(course_code)
        if student_number in course.get("students", []):
            course["students"].remove(student_number)
        if "grades" in course and student_number in course["grades"]:
            del course["grades"][student_number]

    save_data(STUDENTS_FILE, students)
    save_data(COURSES_FILE, courses)
    return {"message": "Dropped"}

def get_students_by_course(course_code: str):
    students_db = load_data(STUDENTS_FILE)
    courses_db = load_data(COURSES_FILE)
    course = next((c for c in courses_db if c["course_code"] == course_code), None)
    if not course: return []

    enrolled_ids = course.get("students", [])
    grades = course.get("grades", {})
    result = []
    for s in students_db:
        if s["student_number"] in enrolled_ids:
            s_data = s.copy()
            s_data["grade"] = grades.get(s["student_number"])
            result.append(s_data)
    return result

def update_student_grade(student_number: str, course_code: str, grade: float):
    courses = load_data(COURSES_FILE)
    course = next((c for c in courses if c["course_code"] == course_code), None)
    if not course: raise HTTPException(status_code=404, detail="Course not found")

    if "grades" not in course: course["grades"] = {}
    course["grades"][student_number] = grade
    save_data(COURSES_FILE, courses)
    return {"message": "Grade updated"}
