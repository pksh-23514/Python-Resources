# Write a program to return the sum of the numbers in an array except ignore the sections of numbers starting with 6 and extending to the next 9.
# Note: Every 6 will be followed by at least one 9. Return 0 for no numbers.
# I/P: summer_69([1, 3, 5])
# O/P: 9
# I/P: summer_69([4, 5, 6, 7, 8, 9])
# O/P: 9
# I/P: summer_69([2, 1, 6, 9, 11])
# O/P: 14
# I/P: summer_69([])
# O/P: 0
# I/P: summer_69([9, 3, 5, 6, 8, 9])
# O/P: 17
# I/P: summer_69([6, 9])
# O/P: 0
# I/P: summer_69([6])
# O/P: 0

"""
**************************************************************
**************************************************************
"""

def summer_69 (array):
    total = 0
    index = 0
    end = len (array)
    while (index < end):
        if (array [index] == 6):
            index += 1
            while (index < end):
                if (array [index] == 9):
                    break
                index += 1
        else:
            total += array [index]
        index += 1
    return total

print (summer_69 ([1, 3, 5]))
print (summer_69 ([4, 5, 6, 7, 8, 9]))
print (summer_69 ([2, 1, 6, 9, 11]))
print (summer_69 ([]))
print (summer_69 ([9, 3, 5, 6, 8, 9]))
print (summer_69 ([6, 9]))
print (summer_69 ([6]))
