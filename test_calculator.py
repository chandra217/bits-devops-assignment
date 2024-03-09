"""
Calculator Application

This defines the Calculator class for performing basic arithmetic operations.
"""

# test_calculator.py
import unittest
from calculator import Calculator

# TestCalculator Class
class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""

    # setup method
    def setUp(self):
        """Set up method to create an instance of Calculator."""
        self.calculator = Calculator()

    # test_add method
    def test_add(self):
        """Test addition operation."""
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5)

    # test_subtract method
    def test_subtract(self):
        """Test subtraction operation."""
        result = self.calculator.subtract(5, 3)
        self.assertEqual(result, 2)

    # test_multiply method
    def test_multiply(self):
        """Test multiplication operation."""
        result = self.calculator.multiply(2, 3)
        self.assertEqual(result, 6)

    # test_divide method
    def test_divide(self):
        """Test division operation."""
        result = self.calculator.divide(6, 2)
        self.assertEqual(result, 3)

        with self.assertRaises(ValueError):
            self.calculator.divide(5, 0)

# initiate main
if __name__ == '__main__':
    unittest.main()
