# Write a program to accept 2 coordinates as a pair of Tuples and return the Slope and Distance of the line.
# I/P: coordinate1 = (3,2)
#      coordinate2 = (8,10)
# O/P: Distance = 9.433981132056603
#      Slope = 1.6

"""
**************************************************************
**************************************************************
"""

class Line:
    def __init__ (self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    def distance (self):
        (x1, y1) = self.coor1
        (x2, y2) = self.coor2
        return ((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5)
    def slope (self):
        (x1, y1) = self.coor1
        (x2, y2) = self.coor2
        return ((y2 - y1) / (x2 - x1))

coordinate1 = (3,2)
coordinate2 = (8,10)
line = Line (coordinate1, coordinate2)
print (f"Distance = {line.distance ()}")
print (f"Slope = {line.slope ()}")
