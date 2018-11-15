"""
Author: Gerard Sharpe
File: triangle_test.py
Purpose: Unit tests for the Triangle class.
Credit:
 Based on code provided by Nicholas Russo Safari Live Training - Python By Example
 https://github.com/nickrusso42518/slt-py-example
"""

from unittest import TestCase
from shapes.triangle import Triangle

class TriangleTest(TestCase):
    """
    Defines a test case for the Triangle class.
    """

    def setUp(self):
        """
        Create a few test objects.
        """
        self.sidea7sideb8sidec9 = Triangle(7, 8, 9)
        self.sidea3sideb4sidec5 = Triangle(3, 4, 5)
        self.sidea9sideb9sidec9 = Triangle(9, 9, 9)
        self.sidea1sideb100sidec3 = Triangle(1, 100, 3)
        self.sidea0sideb10sidec3 = Triangle(0, 10, 3)

    def test_area(self):
        """
        Compare the test triangle area computations to the actual values.
        """
        self.assertEqual(self.sidea7sideb8sidec9.area(), 26.83)
        self.assertEqual(self.sidea3sideb4sidec5.area(), 6.0)
        self.assertEqual(self.sidea9sideb9sidec9.area(), 35.07)
        self.assertEqual(self.sidea1sideb100sidec3.area(), 0)
        self.assertEqual(self.sidea0sideb10sidec3.area(), 0)

    def test_perimeter(self):
        """
        Compare the test triangle perimeter computations to the actual values.
        """
        self.assertEqual(self.sidea7sideb8sidec9.perimeter(), 24)
        self.assertEqual(self.sidea3sideb4sidec5.perimeter(), 12)
        self.assertEqual(self.sidea9sideb9sidec9.perimeter(), 27)
        self.assertEqual(self.sidea1sideb100sidec3.perimeter(), 0)
        self.assertEqual(self.sidea0sideb10sidec3.perimeter(), 0)

    def test_is_rightangle(self):
        """
        Confirm or deny if the triangle has a right angle.
        """
        self.assertEqual(self.sidea7sideb8sidec9.is_rightangle(), False)
        self.assertEqual(self.sidea3sideb4sidec5.is_rightangle(), True)
        self.assertEqual(self.sidea9sideb9sidec9.is_rightangle(), False)
        self.assertEqual(self.sidea1sideb100sidec3.is_rightangle(), False)
        self.assertEqual(self.sidea0sideb10sidec3.is_rightangle(), False)

    def test_is_triangle(self):
        """
        Confirm or deny whether it is a triangle
        """
        self.assertEqual(self.sidea7sideb8sidec9.is_triangle(), True)
        self.assertEqual(self.sidea3sideb4sidec5.is_triangle(), True)
        self.assertEqual(self.sidea9sideb9sidec9.is_triangle(), True)
        self.assertEqual(self.sidea1sideb100sidec3.is_triangle(), False)
        self.assertEqual(self.sidea0sideb10sidec3.is_triangle(), False)
