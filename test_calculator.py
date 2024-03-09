# test_calculator.py
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        result = self.calculator.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiply(self):
        result = self.calculator.multiply(2, 3)
        self.assertEqual(result, 6)

    def test_divide(self):
        result = self.calculator.divide(6, 2)
        self.assertEqual(result, 3)

        with self.assertRaises(ValueError):
            self.calculator.divide(5, 0)

if __name__ == '__main__':
    unittest.main()
