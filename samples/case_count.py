# Write a program that accepts a string and calculates the number of upper case letters and lower case letters.
# I/P: 'Hello Mr. Rogers, how are you this fine Tuesday?'
# O/P: Original String : Hello Mr. Rogers, how are you this fine Tuesday?
#      No. of Upper case characters : 4
#      No. of Lower case characters : 33

"""
**************************************************************
**************************************************************
"""

def count_up_low (sentence):
    lower_count = 0
    upper_count = 0
    for char in sentence:
        if (char.isupper ()):
            upper_count += 1
        elif (char.islower ()):
            lower_count += 1
        else:
            pass
    print (f"Original String : {sentence}")
    print (f"No. of Upper case characters : {upper_count}")
    print (f"No. of Lower case characters : {lower_count}")

count_up_low ("Hello Mr. Rogers, how are you this fine Tuesday?")
