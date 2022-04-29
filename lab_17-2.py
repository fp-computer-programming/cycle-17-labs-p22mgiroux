# Author: MOG 4/28/22

import math

class Circle:
    """ Circle class represents a circle """
    
    def __init__(self, rad):
        """ Create a new circle with radius 1 """
        self.radius = rad

    def get_diameter(self):
        """ Calculate diameter of circle """
        return self.radius * 2

    def get_area(self):
        """ Calculate area of circle """
        return self.radius ** 2 * math.pi

    def get_perimeter(self):
        """ Calculate perimeter of circle """
        return self.get_diameter() * math.pi

my_circle = Circle(3)

print(my_circle.get_perimeter())