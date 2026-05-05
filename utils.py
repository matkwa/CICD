"""
Utility module providing basic arithmetic operations.
"""


def add(a: int, b: int) -> int:
    """
    Add two integers.
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """
    Subtract the second integer from the first.
    """
    return a - b


def multiply(a: int, b: int) -> int:
    """
    Multiply two integers.
    """
    return a * b


def divide(a: int, b: int) -> float:
    """
    Divide the first number by the second.
    """
    return a / b


def to_binary(n: int) -> str:
    """Converts a natural number (0-100) to binary."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Liczba musi być naturalna (całkowita).")

    if n < 0 or n > 100:
        raise ValueError("Liczba musi byc z zakresu od 0 do 100.")

    return bin(n)[2:]
