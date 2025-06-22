# Objective: Enhance your understanding of polymorphism in Python by creating a set of classes
# that demonstrate method overriding and polymorphic behavior.

# Task Description:
# You are tasked with creating a Python script named polymorphism_demo.py.
# In this script, define a base class Shape with a method area() and derived classes Rectangle and Circle,
# each overriding the area() method to calculate their respective areas.

# polymorphism_demo.py:
# Base Class - Shape:

# Method: area(self), which simply raises a NotImplementedError, indicating that derived classes need to override this method.

# Derived Class - Rectangle:
# Inherits from Shape.
# Attributes: length and width.
# Overrides the area() method to calculate the rectangle’s area using the formula: length × width.

# Derived Class - Circle:
# Inherits from Shape.
# Attributes: radius.
# Overrides the area() method to calculate the circle’s area using the formula: π × radius² (use math.pi for π).

import math

class Shape:
    def area(self):
        """Method to calculate the area of the shape. Should be overridden by derived classes."""
        raise NotImplementedError("This method should be overridden by derived classes.")
    
class Rectangle(Shape):
    def __init__(self, length: float, width: float) -> None:
        """Constructor to initialize the rectangle's length and width."""
        self.length = length
        self.width = width
    
    def area(self) -> float:
        """Calculate the area of the rectangle."""
        return self.length * self.width
    

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        """Constructor to initialize the circle's radius."""
        self.radius = radius
    
    def area(self) -> float:
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
