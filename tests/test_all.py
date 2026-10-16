import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from calculator import add, divide, multiply, subtract
from text_utils import factorial, is_palindrome, word_frequency
from todo import TodoList


class TestCalculator(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(divide(10, 4), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(1, 0)


class TestTodo(unittest.TestCase):
    def test_add_and_complete(self):
        todo = TodoList()
        todo.add("Task 1")
        todo.add("Task 2")
        todo.complete(1)
        self.assertEqual(len(todo.pending()), 1)

    def test_empty_title(self):
        with self.assertRaises(ValueError):
            TodoList().add("   ")

    def test_missing_id(self):
        with self.assertRaises(KeyError):
            TodoList().complete(99)


class TestTextUtils(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome("hello"))

    def test_word_frequency(self):
        self.assertEqual(word_frequency("to be or not to be")["to"], 2)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)


if __name__ == "__main__":
    unittest.main()
