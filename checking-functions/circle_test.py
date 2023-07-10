import unittest
from circle import *

class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(10), 314.159 )
    def test_perimeter(self):
        self.assertAlmostEqual(getPerimeter(10), 314.159 )
        
unittest.main()