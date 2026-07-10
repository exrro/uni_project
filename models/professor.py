from models.person import Person


class Professor(Person):
    def __init__(
        self,
        national_id: str,
        first_name: str,
        last_name: str,
        professor_code: str,
        department: str,
        courses: list[str] | None = None,
    ):
        super().__init__(national_id, first_name, last_name)
        self.professor_code = professor_code
        self.department = department
        self.courses = courses or []

    def add_course(self, course_code: str) -> None:
        if course_code not in self.courses:
            self.courses.append(course_code)

    def remove_course(self, course_code: str) -> None:
        if course_code in self.courses:
            self.courses.remove(course_code)

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update(
            {
                "professor_code": self.professor_code,
                "department": self.department,
                "courses": self.courses,
            }
        )
        return data
