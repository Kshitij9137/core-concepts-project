"""Mini project 1: Calculator - functions, error handling, input validation."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("10 + 15 =", add(10, 15))
    print("10 / 4 =", divide(10, 4))
