# Write a program to return True if the number is within 10 of either 100 or 200, otherwise False.
# I/P: almost_there(90)
# O/P: True
# I/P: almost_there(104)
# O/P: True
# I/P: almost_there(150)
# O/P: False
# I/P: almost_there(209)
# O/P: True

"""
**************************************************************
**************************************************************
"""

def almost_there (num):
    if ((abs (num - 100) <= 10) or (abs (num - 200) <= 10)):
        return True
    else:
        return False

print (almost_there (90))
print (almost_there (104))
print (almost_there (150))
print (almost_there (209))
