import pytest

from app import Student


def test_total() -> None:
    student = Student("Anish", [90, 80, 70])

    assert student.total() == 240


def test_average() -> None:
    student = Student("Anish", [90, 80, 70])

    assert student.average() == 80


def test_grade_a() -> None:
    student = Student("Anish", [95, 92, 90])

    assert student.grade() == "A"


def test_grade_b() -> None:
    student = Student("Anish", [85, 82, 80])

    assert student.grade() == "B"


def test_grade_c() -> None:
    student = Student("Anish", [75, 72, 70])

    assert student.grade() == "C"


def test_grade_d() -> None:
    student = Student("Anish", [65, 62, 60])

    assert student.grade() == "D"


def test_grade_f() -> None:
    student = Student("Anish", [50, 55, 40])

    assert student.grade() == "F"


def test_invalid_mark() -> None:
    with pytest.raises(ValueError):
        Student("Anish", [90, 120, 80])


def test_negative_mark() -> None:
    with pytest.raises(ValueError):
        Student("Anish", [90, -10, 80])


def test_empty_name() -> None:
    with pytest.raises(ValueError):
        Student("", [90, 80, 70])


def test_empty_marks() -> None:
    with pytest.raises(ValueError):
        Student("Anish", [])