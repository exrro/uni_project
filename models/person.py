class Person:
    def __init__(self, national_id: str, first_name: str, last_name: str):
        self.national_id = national_id
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def to_dict(self) -> dict:
        return {
            "national_id": self.national_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "full_name": self.full_name,
        }
