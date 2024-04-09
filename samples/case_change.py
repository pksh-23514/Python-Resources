# Write a program that takes in a String and returns a matching string where every Even letter is Uppercase, and every Odd letter is Lowercase.
# Assume that the input String only contains letters and don't worry about numbers, spaces or punctuation.

# I/P: 'Anthropomorphism'
# O/P: 'aNtHrOpOmOrPhIsM'

"""
**************************************************************
**************************************************************
"""

def my_func (my_str):
    result_str = ""
    for index in range (0, len (my_str)):
        if ((index + 1) % 2 == 0):
            result_str += my_str [index].upper ()
        else:
            result_str += my_str [index].lower ()
    return result_str

my_str = 'Anthropomorphism'
result_str = my_func (my_str)

print (f"I/P: {my_str}")
print (f"O/P: {result_str}")
