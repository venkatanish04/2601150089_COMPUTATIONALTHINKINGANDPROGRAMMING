import pytest

from student import Student, StudentManager


# ---------------- UNIT TESTS ----------------

def test_total_marks() -> None:
    student = Student(1, "Anish", [80, 90, 70])

    assert student.total() == 240


def test_average_marks() -> None:
    student = Student(1, "Anish", [80, 90, 70])

    assert student.average() == 80


@pytest.mark.parametrize(
    "marks, expected_grade",
    [
        ([95, 92, 90], "A"),
        ([85, 82, 80], "B"),
        ([75, 72, 70], "C"),
        ([65, 62, 60], "D"),
        ([50, 55, 40], "F"),
    ],
)
def test_grade(
    marks: list[float],
    expected_grade: str,
) -> None:
    student = Student(1, "Anish", marks)

    assert student.grade() == expected_grade


def test_invalid_marks() -> None:
    with pytest.raises(ValueError):
        Student(1, "Anish", [80, 120, 90])


def test_negative_marks() -> None:
    with pytest.raises(ValueError):
        Student(1, "Anish", [80, -10, 90])


def test_empty_name() -> None:
    with pytest.raises(ValueError):
        Student(1, "", [80, 90])


# ---------------- INTEGRATION TESTS ----------------

def test_add_student() -> None:
    manager = StudentManager()

    student = Student(1, "Anish", [80, 90, 85])

    manager.add_student(student)

    assert manager.get_student(1) == student
    assert manager.student_count() == 1


def test_duplicate_student() -> None:
    manager = StudentManager()

    student = Student(1, "Anish", [80, 90])

    manager.add_student(student)

    with pytest.raises(ValueError):
        manager.add_student(student)


def test_remove_student() -> None:
    manager = StudentManager()

    student = Student(1, "Anish", [80, 90])

    manager.add_student(student)
    manager.remove_student(1)

    assert manager.student_count() == 0


def test_student_not_found() -> None:
    manager = StudentManager()

    with pytest.raises(ValueError):
        manager.get_student(999)