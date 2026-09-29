from app import add, greet


def test_add() -> None:
    assert add(10, 20) == 30


def test_greet() -> None:
    assert greet("Anish") == "Hello, Anish"


def test_add_zero() -> None:
    assert add(0, 0) == 0