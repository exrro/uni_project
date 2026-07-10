from pydantic import BaseModel, Field


class ProfessorCreate(BaseModel):
    national_id: str = Field(..., min_length=10, max_length=10)
    first_name: str
    last_name: str
    professor_code: str
    department: str


class ProfessorUpdate(BaseModel):
    national_id: str | None = Field(default=None, min_length=10, max_length=10)
    first_name: str | None = None
    last_name: str | None = None
    department: str | None = None
