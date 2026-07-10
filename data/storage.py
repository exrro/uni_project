import json
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STUDENTS_FILE = os.path.join(BASE_DIR, "students.json")
PROFESSORS_FILE = os.path.join(BASE_DIR, "professors.json")
COURSES_FILE = os.path.join(BASE_DIR, "courses.json")


def ensure_file_exists(file_path: str) -> None:
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=2)


def load_data(file_path: str) -> list[dict]:
    ensure_file_exists(file_path)
    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
        except json.JSONDecodeError:
            return []


def save_data(file_path: str, data: list[dict]) -> None:
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
