"""
Author: Gerard Sharpe
File: triangle.py
Purpose: Defines a Triangle object, inherited from the abstract class Shape.
Credit:
 Based on code provided by Nicholas Russo Safari Live Training - Python By Example
 https://github.com/nickrusso42518/slt-py-example
"""

from math import sqrt
from shapes.shape import Shape


class Triangle(Shape):
    """
    Represents a Triangle shape, and contains three side values
    """
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def is_triangle(self):
        """
        A triangle is valid if sum of it's two sides are greater than the third side.
        """
        return self.side_a + self.side_b > self.side_c and \
               self.side_a + self.side_c > self.side_b and \
               self.side_b + self.side_c > self.side_a

    def area(self):
        """
        Compute the area using Heron's formula
        """
        if(self.is_triangle()):
            self.semiperimeter = self.perimeter() / 2
            self.area = sqrt(self.semiperimeter * (self.semiperimeter - self.side_a) * \
                             (self.semiperimeter - self.side_b) * (self.semiperimeter - self.side_c))
            self.area = round(self.area, 2)
            return self.area
        else:
            return 0

    def perimeter(self):
        """
        Compute the perimeter
        """
        if(self.is_triangle()):
            self.perimeter = self.side_a + self.side_b + self.side_c
            return round(self.perimeter, 2)
        else:
            return 0

    def is_rightangle(self):
        """
        Determine if the triangle is a right angled triangles by using the Pythagorean theorem
        which states if and only if a^2 + b^2 == c^2 then the triangle is a right triangle.
        """
        if(self.is_triangle()):
            return self.side_a ^ 2 + self.side_b ^ 2 == self.side_c ^ 2
        else:
            return False
