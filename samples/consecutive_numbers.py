# Write a program to return True if the array contains 2 consecutive '3', otherwise False.
# I/P: has_33([1, 3, 3])
# O/P: True
# I/P: has_33([1, 3, 1, 3])
# O/P: False
# I/P: has_33([3, 1, 3])
# O/P: False

"""
**************************************************************
**************************************************************
"""

def has_33 (array):
    for i in range (0, (len (array) - 1)):
        if ((array [i] == 3) and (array [i+1] == 3)):
            return True
    return False

print (has_33 ([1, 3, 3]))
print (has_33 ([1, 3, 1, 3]))
print (has_33([3, 1, 3]))
