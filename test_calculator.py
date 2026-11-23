import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(5, 3), 8)

    def test_subtract(self):
        calc = Calculator()
        self.assertEqual(calc.subtract(5, 3), 2)

    def test_multiply(self):
        calc = Calculator()
        self.assertEqual(calc.multiply(5, 3), 15)

    def test_divide(self):
        calc = Calculator()
        self.assertEqual(calc.divide(6, 3), 2)

    def test_divide_by_zero(self):
        calc = Calculator()
        self.assertEqual(calc.divide(5, 0), "Cannot divide by zero")


if __name__ == "__main__":
    unittest.main()
