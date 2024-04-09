# Write a program to count the number of Prime numbers that exist upto and including the given number.
# Note: By convention, 0 and 1 are considered not Prime.
# I/P: 100
# O/P: 25

"""
**************************************************************
**************************************************************
"""

def is_Prime (num):
    div = 2
    while ((div * div) <= num):
        if ((num % div) == 0):
            return False
        div += 1
    return True

def count_Prime (limit):
    prime = [2]
    num = 3
    if (limit < 2):
        return 0
    else:
        while (num <= limit):
            if (is_Prime (num) == True):
                prime.append (num)
            num += 1
    print (prime)
    return len (prime)

print (count_Prime (100))
