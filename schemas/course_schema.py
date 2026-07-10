from pydantic import BaseModel, Field


class CourseCreate(BaseModel):
    course_code: str
    title: str
    units: int = Field(..., ge=1, le=6)
    professor_code: str | None = None


class CourseUpdate(BaseModel):
    title: str | None = None
    units: int | None = Field(default=None, ge=1, le=6)
    professor_code: str | None = None
