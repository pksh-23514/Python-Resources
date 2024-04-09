# Write a program to return a string where for every character in the original, there are three characters.
# I/P: paper_doll('Hello')
# O/P: 'HHHeeellllllooo'
# I/P: paper_doll('Mississippi')
# O/P: 'MMMiiissssssiiippppppiii'

"""
**************************************************************
**************************************************************
"""

def paper_doll (string):
    new_str = ""
    for char in string:
        new_str = new_str + (char * 3)
    return new_str

print (paper_doll ('Hello'))
print (paper_doll ('Mississippi'))
