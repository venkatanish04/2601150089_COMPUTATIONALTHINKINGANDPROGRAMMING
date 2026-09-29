def add(a: int, b: int) -> int:
    return a + b


def greet(name: str) -> str:
    return f"Hello, {name}!"


def main() -> None:
    result: int = add(10, 20)

    print(greet("Anish"))
    print("Result:", result)


if __name__ == "__main__":
    main()