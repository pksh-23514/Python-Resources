# Write a program that takes a List of numbers and returns a new sequence of unique elements of the initial List.
# I/P: [1,1,1,1,2,2,3,3,3,3,4,5]
# O/P: [1, 2, 3, 4, 5]

"""
**************************************************************
**************************************************************
"""

def unique_list (my_list):
    new_list = []
    for num in my_list:
        if (num not in new_list):
            new_list.append (num)
    return new_list

print (unique_list ([1,1,1,1,2,2,3,3,3,3,4,5]))


# **************************************************************
# **************************************************************
# Using the Set Data-type, this can be solved in one line:
# return (list ((set (my_list))))
# **************************************************************
# **************************************************************
