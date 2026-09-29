from dataclasses import dataclass, asdict
@dataclass
class Student:
    student_id: int
    name: str
    course: str
    marks: float

@dataclass
class Employee:
    employee_id: int
    name: str
    department: str
    salary: float

class TraditionalStudent:
    def __init__(
        self,
        student_id: int,
        name: str,
        course: str,
        marks: float
    ) -> None:
        self.student_id = student_id
        self.name = name
        self.course = course
        self.marks = marks

    def __repr__(self) -> str:
        return (
            f"TraditionalStudent("
            f"student_id={self.student_id}, "
            f"name='{self.name}', "
            f"course='{self.course}', "
            f"marks={self.marks})"
        )
class TraditionalEmployee:
    def __init__(
        self,
        employee_id: int,
        name: str,
        department: str,
        salary: float
    ) -> None:
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary

    def __repr__(self) -> str:
        return (
            f"TraditionalEmployee("
            f"employee_id={self.employee_id}, "
            f"name='{self.name}', "
            f"department='{self.department}', "
            f"salary={self.salary})"
        )
def main() -> None:

    # Dataclass objects
    student = Student(
        student_id=101,
        name="Anish",
        course="CSE",
        marks=88.5
    )

    employee = Employee(
        employee_id=501,
        name="Venkat",
        department="IT",
        salary=50000.0
    )

    # Traditional class objects
    traditional_student = TraditionalStudent(
        101,
        "Anish",
        "CSE",
        88.5
    )

    traditional_employee = TraditionalEmployee(
        501,
        "Venkat",
        "IT",
        50000.0
    )

    print("Student:", student)
    print("Employee:", employee)

    # Convert dataclass objects to dictionaries
    print("\nDataclass Student Dictionary:")
    print(asdict(student))

    print("\nDataclass Employee Dictionary:")
    print(asdict(employee))

    # Display Traditional class objects
    print("\n===== TRADITIONAL CLASS IMPLEMENTATION =====")
    print("Student:", traditional_student)
    print("Employee:", traditional_employee)

    # Comparison
    print("\n===== COMPARISON =====")
    print("1. Dataclass requires less code.")
    print("2. Dataclass automatically generates __init__().")
    print("3. Dataclass automatically generates __repr__().")
    print("4. Dataclass provides asdict() for easy conversion.")
    print("5. Traditional classes provide more manual control.")


if __name__ == "__main__":
    main()