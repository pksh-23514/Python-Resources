# Write a program that returns:
# (1) Lesser of the two given numbers if both the numbers are Even.
# (2) Greater of the two given numbers if one or both the numbers are Odd.
# I/P: lesser_of_two_evens(2,4)
# O/P: 2
# I/P: lesser_of_two_evens(2,5)
# O/P: 5
# I/P: lesser_of_two_evens(7,5)
# O/P: 7

"""
**************************************************************
**************************************************************
"""

def is_Even (num):
    if (num % 2 == 0):
        return True

def lesser_of_two_evens (x, y):
    if ((is_Even (x)) and (is_Even (y))):
        return (x if (x < y) else y)
    else:
        return (x if (x > y) else y)

print (lesser_of_two_evens (7, 5))
print (lesser_of_two_evens (2, 5))
print (lesser_of_two_evens (2, 4))
