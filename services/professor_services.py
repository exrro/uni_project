from fastapi import HTTPException

from data.storage import PROFESSORS_FILE, COURSES_FILE, load_data, save_data
from models.professor import Professor


def _find_professor_index(professors: list[dict], professor_code: str) -> int:
    for index, professor in enumerate(professors):
        if professor["professor_code"] == professor_code:
            return index
    return -1


def get_all_professors() -> list[dict]:
    return load_data(PROFESSORS_FILE)


def get_professor_by_code(professor_code: str) -> dict:
    professors = load_data(PROFESSORS_FILE)
    for professor in professors:
        if professor["professor_code"] == professor_code:
            return professor
    raise HTTPException(status_code=404, detail="Professor not found")


def create_professor(
    national_id: str,
    first_name: str,
    last_name: str,
    professor_code: str,
    department: str,
) -> dict:
    professors = load_data(PROFESSORS_FILE)

    for professor in professors:
        if professor["professor_code"] == professor_code:
            raise HTTPException(status_code=400, detail="Professor already exists")
        if professor["national_id"] == national_id:
            raise HTTPException(status_code=400, detail="National ID already exists")

    new_professor = Professor(
        national_id=national_id,
        first_name=first_name,
        last_name=last_name,
        professor_code=professor_code,
        department=department,
    )

    professors.append(new_professor.to_dict())
    save_data(PROFESSORS_FILE, professors)
    return new_professor.to_dict()


def update_professor(professor_code: str, update_data: dict) -> dict:
    professors = load_data(PROFESSORS_FILE)
    professor_index = _find_professor_index(professors, professor_code)

    if professor_index == -1:
        raise HTTPException(status_code=404, detail="Professor not found")

    current_professor = professors[professor_index]

    new_national_id = update_data.get("national_id", current_professor["national_id"])
    if new_national_id != current_professor["national_id"]:
        for professor in professors:
            if professor["national_id"] == new_national_id:
                raise HTTPException(status_code=400, detail="National ID already exists")

    current_professor["national_id"] = new_national_id
    current_professor["first_name"] = update_data.get("first_name", current_professor["first_name"])
    current_professor["last_name"] = update_data.get("last_name", current_professor["last_name"])
    current_professor["department"] = update_data.get("department", current_professor["department"])
    current_professor["full_name"] = f"{current_professor['first_name']} {current_professor['last_name']}"

    professors[professor_index] = current_professor
    save_data(PROFESSORS_FILE, professors)
    return current_professor


def delete_professor(professor_code: str) -> dict:
    professors = load_data(PROFESSORS_FILE)
    courses = load_data(COURSES_FILE)

    professor_index = _find_professor_index(professors, professor_code)
    if professor_index == -1:
        raise HTTPException(status_code=404, detail="Professor not found")

    for course in courses:
        if course["professor_code"] == professor_code:
            course["professor_code"] = None

    save_data(COURSES_FILE, courses)

    deleted_professor = professors.pop(professor_index)
    save_data(PROFESSORS_FILE, professors)

    return {
        "message": "Professor deleted successfully",
        "professor": deleted_professor,
    }
