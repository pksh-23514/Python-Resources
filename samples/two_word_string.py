# Write a program that takes a 2 word String and returns True if both the word begins with the same letter, otherwise False.
# I/P: animal_check('Levelheaded Llama')
# O/P: True
# I/P: animal_check('Crazy Kangaroo')
# O/P: False

"""
**************************************************************
**************************************************************
"""

def animal_check (text):
    words = text.lower ()
    words = text.split ()
    if (words [0][0] == words [1][0]):
        return True
    else:
        return False

print (animal_check ('Levelheaded Llama'))
print (animal_check ('Crazy Kangaroo'))
