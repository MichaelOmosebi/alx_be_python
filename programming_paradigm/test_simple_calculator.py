# Create a test_simple_calculator.py script to define and run unit tests for each method in the SimpleCalculator class. Your tests should cover various scenarios to ensure the class functions correctly.

# Guidelines for Writing Tests:
# Import the Necessary Modules:

# Import the unittest module and the SimpleCalculator class from simple_calculator.py.
# Define a Test Class:

# Create a test class that inherits from unittest.TestCase.
# Write Test Methods:

# Write at least one test method for each operation (add, subtract, multiply, divide) provided by the SimpleCalculator.
# Include tests for edge cases, such as dividing by zero.
# Use Assertions to Verify Results:

# Utilize self.assertEqual() to check for expected outcomes.
# For the divide method, ensure you test both normal operation and division by zero.
# Running Your Tests:

# Run your tests using the command line: python -m unittest test_simple_calculator.py.

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Create an instance of SimpleCalculator for testing."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtract(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiply(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_divide(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero should return None


if __name__ == "__main__":
  unittest.main()
# test_simple_calculator.py doesn't contain: ["test_addition", "test_addition(self)"]

