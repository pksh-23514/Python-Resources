# Write a program that returns:
# (1) Returns True if the sum of the integers is 20 or if one of the integers is 20.
# (2) Returns False if otherwise.
# I/P: makes_twenty(20,10)
# O/P: True
# I/P: makes_twenty(12,8)
# O/P: True
# I/P: makes_twenty(2,3)
# O/P: False

"""
**************************************************************
**************************************************************
"""

def makes_twenty (num1, num2):
    if ((num1 == 20) or (num2 == 20) or ((num1 + num2) == 20)):
        return True
    else:
        return False

print (makes_twenty (20,10))
print (makes_twenty (12,8))
print (makes_twenty (2,3))
