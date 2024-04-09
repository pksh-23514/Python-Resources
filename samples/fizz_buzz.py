# Write a program that prints the integers from 1 to 100 based on the below criteria:
# (1) For the multiples of three, print "Fizz" instead of the number.
# (2) For the multiples of five, print "Buzz" instead of the number.
# (3) For the multiples of both three and five, print "FizzBuzz" instead of the number.

# I/P: 15
# O/P: FizzBuzz
# I/P: 3
# O/P: Fizz
# I/P: 5
# O/P: Buzz
# I/P: 2
# O/P: 2

"""
**************************************************************
**************************************************************
"""

for num in range (1, 101):
    if ((num % 3 == 0) and (num % 5 == 0)):
        print ("FizzBuzz", end=' ')
    elif (num % 3 == 0):
        print ("Fizz", end=' ')
    elif (num % 5 == 0):
        print ("Buzz", end=' ')
    else:
        print (num, end=' ')
print ("")
