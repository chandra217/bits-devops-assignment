"""
Calculator Application

This defines the Calculator class for performing basic arithmetic operations.
"""

# Calculator class
class Calculator:
    """
    This class represents a simple calculator.
    """
    # add function
    def add(self, a, b):
        """
        Adds two numbers.
        """
        return a + b

    # subtract function
    def subtract(self, a, b):
        """
        Subtracts two numbers.
        """
        return a - b

    # multiply function
    def multiply(self, a, b):
        """
        Multiplies two numbers.
        """
        return a * b

    # divide function
    def divide(self, a, b):
        """
        Divides two numbers.
        Raises a ValueError if b is zero.
        """
        if b != 0:
            return a / b
        raise ValueError("Cannot divide by zero")
