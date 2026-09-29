from dataclasses import dataclass


@dataclass
class Student:
    student_id: int
    name: str
    marks: list[float]

    def __post_init__(self) -> None:
        if self.student_id <= 0:
            raise ValueError("Student ID must be positive.")

        if not self.name.strip():
            raise ValueError("Student name cannot be empty.")

        if not self.marks:
            raise ValueError("Marks cannot be empty.")

        if any(mark < 0 or mark > 100 for mark in self.marks):
            raise ValueError("Marks must be between 0 and 100.")

    def total(self) -> float:
        return sum(self.marks)

    def average(self) -> float:
        return self.total() / len(self.marks)

    def grade(self) -> str:
        average = self.average()

        if average >= 90:
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        if average >= 60:
            return "D"

        return "F"


class StudentManager:
    def __init__(self) -> None:
        self.students: dict[int, Student] = {}

    def add_student(self, student: Student) -> None:
        if student.student_id in self.students:
            raise ValueError("Student already exists.")

        self.students[student.student_id] = student

    def get_student(self, student_id: int) -> Student:
        if student_id not in self.students:
            raise ValueError("Student not found.")

        return self.students[student_id]

    def remove_student(self, student_id: int) -> None:
        if student_id not in self.students:
            raise ValueError("Student not found.")

        del self.students[student_id]

    def student_count(self) -> int:
        return len(self.students)