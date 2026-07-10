from fastapi import APIRouter
from services import course_services
from schemas.course_schema import CourseCreate, CourseUpdate
from services.course_services import (
    create_course,
    delete_course,
    get_all_courses,
    get_course_by_code,
    update_course,
)

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.get("/")
def read_courses():
    return get_all_courses()


@router.get("/{course_code}")
def read_course(course_code: str):
    return get_course_by_code(course_code)


@router.post("/")
def add_course(course: CourseCreate):
    return create_course(
        course_code=course.course_code,
        title=course.title,
        units=course.units,
        professor_code=course.professor_code,
    )


@router.put("/{course_code}")
def edit_course(course_code: str, course: CourseUpdate):
    return update_course(course_code, course.model_dump(exclude_unset=True))


@router.delete("/{course_code}")
def remove_course(course_code: str):
    return delete_course(course_code)
