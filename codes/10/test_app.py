from app import calculate_total, greet


def test_calculate_total() -> None:
    assert calculate_total([10, 20, 30]) == 60


def test_empty_list() -> None:
    assert calculate_total([]) == 0


def test_greet() -> None:
    assert greet("Anish") == "Hello, Anish!"