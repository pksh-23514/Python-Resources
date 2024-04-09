# Write a program that takes an array of integers and returns True if it contains "007" in order, otherwise False.
# I/P: spy_game([1, 2, 4, 0, 0, 7, 5])
# O/P: True
# I/P: spy_game([1, 0, 2, 4, 0, 5, 7])
# O/P: True
# I/P: spy_game([1, 7, 2, 0, 4, 5, 0])
# O/P: False

"""
**************************************************************
**************************************************************
"""

def spy_game (array):
    ref = [0, 0, 7, "END"]
    for num in array:
        if (num == ref [0]):
            ref.pop (0)
    if (len (ref) == 1):
        return True
    else:
        return False

print (spy_game ([1, 2, 4, 0, 0, 7, 5]))
print (spy_game ([1, 0, 2, 4, 0, 5, 7]))
print (spy_game ([1, 7, 2, 0, 4, 5, 0]))
