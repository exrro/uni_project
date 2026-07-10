from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    national_id: str = Field(..., min_length=10, max_length=10)
    first_name: str
    last_name: str
    student_number: str
    major: str


class StudentUpdate(BaseModel):
    national_id: str | None = Field(default=None, min_length=10, max_length=10)
    first_name: str | None = None
    last_name: str | None = None
    major: str | None = None
