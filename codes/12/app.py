from dataclasses import dataclass


@dataclass
class Student:
    name: str
    marks: list[float]

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Student name cannot be empty.")

        if not self.marks:
            raise ValueError("Marks cannot be empty.")

        for mark in self.marks:
            if mark < 0 or mark > 100:
                raise ValueError(
                    "Marks must be between 0 and 100."
                )

    def total(self) -> float:
        """Return the total marks."""
        return sum(self.marks)

    def average(self) -> float:
        """Return the average marks."""
        return self.total() / len(self.marks)

    def grade(self) -> str:
        """Return the grade based on average marks."""
        average: float = self.average()

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"


def display_student(student: Student) -> None:
    """Display student information."""

    print("\n===== STUDENT REPORT =====")
    print(f"Name    : {student.name}")
    print(f"Marks   : {student.marks}")
    print(f"Total   : {student.total():.2f}")
    print(f"Average : {student.average():.2f}")
    print(f"Grade   : {student.grade()}")


def main() -> None:
    name: str = input("Enter student name: ")

    marks_input: str = input(
        "Enter marks separated by spaces: "
    )

    marks: list[float] = [
        float(mark)
        for mark in marks_input.split()
    ]

    try:
        student = Student(name, marks)
        display_student(student)

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()