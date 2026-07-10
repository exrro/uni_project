class Course:
    def __init__(
        self,
        course_code: str,
        title: str,
        units: int,
        professor_code: str | None = None,
        students: list[str] | None = None,
    ):
        self.course_code = course_code
        self.title = title
        self.units = units
        self.professor_code = professor_code
        self.students = students or []

    def set_professor(self, professor_code: str | None) -> None:
        self.professor_code = professor_code

    def add_student(self, student_number: str) -> None:
        if student_number not in self.students:
            self.students.append(student_number)

    def remove_student(self, student_number: str) -> None:
        if student_number in self.students:
            self.students.remove(student_number)

    def to_dict(self) -> dict:
        return {
            "course_code": self.course_code,
            "title": self.title,
            "units": self.units,
            "professor_code": self.professor_code,
            "students": self.students,
        }
