from typing import List


def calculate_total(numbers: List[int]) -> int:
    """Return the sum of all numbers."""
    return sum(numbers)


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def main() -> None:
    numbers: List[int] = [10, 20, 30, 40, 50]

    total: int = calculate_total(numbers)

    print(greet("Anish"))
    print(f"Total: {total}")


if __name__ == "__main__":
    main()