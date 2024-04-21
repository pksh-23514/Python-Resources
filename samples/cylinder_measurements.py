# Write a program that takes in the radius and height of a cylinder and returns the volume and surface area of it.
# I/P: c = Cylinder(2,3)
# O/P: Volume = 56.52
#      Surface Area = 94.2

"""
**************************************************************
**************************************************************
"""

from math import pi
class Cylinder:
    def __init__ (self, height=1, radius=1):
        self.height = height
        self.radius = radius
    def volume (self):
        return (pi * (self.radius ** 2) * self.height)
    def surface_area (self):
        return (2 * pi * self.radius * (self.radius + self.height))

c = Cylinder (2,3)
print (f"Volume = {c.volume ()}")
print (f"Surface Area = {c.surface_area ()}")
