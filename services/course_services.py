from fastapi import HTTPException

from data.storage import COURSES_FILE, PROFESSORS_FILE, load_data, save_data
from models.course import Course


def _find_course_index(courses: list[dict], course_code: str) -> int:
    for index, course in enumerate(courses):
        if course["course_code"] == course_code:
            return index
    return -1


def get_all_courses() -> list[dict]:
    return load_data(COURSES_FILE)


def get_course_by_code(course_code: str) -> dict:
    courses = load_data(COURSES_FILE)
    for course in courses:
        if course["course_code"] == course_code:
            return course
    raise HTTPException(status_code=404, detail="Course not found")


def create_course(
    course_code: str,
    title: str,
    units: int,
    professor_code: str | None = None,
) -> dict:
    courses = load_data(COURSES_FILE)
    professors = load_data(PROFESSORS_FILE)

    for course in courses:
        if course["course_code"] == course_code:
            raise HTTPException(status_code=400, detail="Course already exists")

    if professor_code is not None:
        professor_exists = any(
            professor["professor_code"] == professor_code for professor in professors
        )
        if not professor_exists:
            raise HTTPException(status_code=404, detail="Professor not found")

    new_course = Course(
        course_code=course_code,
        title=title,
        units=units,
        professor_code=professor_code,
    )

    courses.append(new_course.to_dict())
    save_data(COURSES_FILE, courses)

    if professor_code is not None:
        for professor in professors:
            if professor["professor_code"] == professor_code:
                if course_code not in professor["courses"]:
                    professor["courses"].append(course_code)
                break
        save_data(PROFESSORS_FILE, professors)

    return new_course.to_dict()


def update_course(course_code: str, update_data: dict) -> dict:
    courses = load_data(COURSES_FILE)
    professors = load_data(PROFESSORS_FILE)

    course_index = _find_course_index(courses, course_code)
    if course_index == -1:
        raise HTTPException(status_code=404, detail="Course not found")

    current_course = courses[course_index]
    old_professor_code = current_course["professor_code"]

    new_title = update_data.get("title", current_course["title"])
    new_units = update_data.get("units", current_course["units"])

    if "professor_code" in update_data:
        new_professor_code = update_data["professor_code"]
        if new_professor_code is not None:
            professor_exists = any(
                professor["professor_code"] == new_professor_code for professor in professors
            )
            if not professor_exists:
                raise HTTPException(status_code=404, detail="Professor not found")
    else:
        new_professor_code = old_professor_code

    current_course["title"] = new_title
    current_course["units"] = new_units
    current_course["professor_code"] = new_professor_code
    courses[course_index] = current_course
    save_data(COURSES_FILE, courses)

    if old_professor_code != new_professor_code:
        for professor in professors:
            if professor["professor_code"] == old_professor_code:
                if course_code in professor["courses"]:
                    professor["courses"].remove(course_code)

        if new_professor_code is not None:
            for professor in professors:
                if professor["professor_code"] == new_professor_code:
                    if course_code not in professor["courses"]:
                        professor["courses"].append(course_code)

        save_data(PROFESSORS_FILE, professors)

    return current_course


def delete_course(course_code: str) -> dict:
    courses = load_data(COURSES_FILE)
    students_file_data = load_data("data/students.json")
    professors = load_data(PROFESSORS_FILE)

    course_index = _find_course_index(courses, course_code)
    if course_index == -1:
        raise HTTPException(status_code=404, detail="Course not found")

    course = courses[course_index]

    for student in students_file_data:
        if course_code in student["selected_courses"]:
            student["selected_courses"].remove(course_code)

    for professor in professors:
        if course_code in professor["courses"]:
            professor["courses"].remove(course_code)

    save_data("data/students.json", students_file_data)
    save_data(PROFESSORS_FILE, professors)

    deleted_course = courses.pop(course_index)
    save_data(COURSES_FILE, courses)

    return {
        "message": "Course deleted successfully",
        "course": deleted_course,
    }
