from models.person import Person


class Student(Person):
    def __init__(
        self,
        national_id: str,
        first_name: str,
        last_name: str,
        student_number: str,
        major: str,
        selected_courses: list[str] | None = None,
    ):
        super().__init__(national_id, first_name, last_name)
        self.student_number = student_number
        self.major = major
        self.selected_courses = selected_courses or []

    def add_course(self, course_code: str) -> None:
        if course_code not in self.selected_courses:
            self.selected_courses.append(course_code)

    def remove_course(self, course_code: str) -> None:
        if course_code in self.selected_courses:
            self.selected_courses.remove(course_code)

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update(
            {
                "student_number": self.student_number,
                "major": self.major,
                "selected_courses": self.selected_courses,
            }
        )
        return data
