"""Mini project 3: Text utilities - strings, file-free data processing, recursion."""
from collections import Counter


def is_palindrome(text: str) -> bool:
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def word_frequency(text: str) -> dict:
    words = [w.strip(".,!?;:").lower() for w in text.split()]
    return dict(Counter(w for w in words if w))


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    return 1 if n in (0, 1) else n * factorial(n - 1)


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(word_frequency("to be or not to be"))
    print(factorial(4))
