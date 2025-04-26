def say_hi ():
    print ("Hello World!")
say_hi ()
print ("")

def say_hello (name='Prabhat'):
    print ("Hello " + name)
say_hello ('Krishna')
say_hello ()
print ("")

def return_result (first, second):
    return (first + second)
add = return_result (14, 23)
print ("Sum: ", add)
print ("")

def print_result (first, second):
    print ("Sum: ", (first + second))
add = print_result (14, 23)
print (add)
print (type (add))
print ("")

def add_num (first, second):
    return (first + second)
print (add_num (14, 23))
print (add_num ('14', '23'))
print ("")

# Return True if any of the number in the List is Even. Otherwise, return False.
def even_check (my_list):
    for num in my_list:
        if ((num % 2) == 0):
            return True
        else:
            pass
    return False
print (even_check ([1, 3, 5]))
print (even_check ([1, 2, 5]))
print ("")

# Return Tuple from a function and Unpack the values.
def emp_work (work_details):
    max_hr = 0
    emp_month = ''
    for (emp, hr) in work_details:
        if (hr > max_hr):
            emp_month = emp
            max_hr = hr
        else:
            pass
    return (emp_month, max_hr)
work_details = [('Naruto', 100), ('Sasuke', 75)]
result = emp_work (work_details)
print (result)
(name, hours) = emp_work (work_details)
print ("Employee of the Month: ", name)
print ("Hours worked: ", hours)
print ("")

# Interaction between multiple Functions.
from random import shuffle

def shuffle_list (my_list):
    shuffle (my_list)
    return my_list

def player_guess ():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input ("Pick any choice between 0, 1 or 2: ")
    return (int (guess))

def check_guess (my_list, guess):
    if (my_list [guess] == 'O'):
        print ("Correct choice!")
    else:
        print ("Wrong choice. Try Again!")
    print (my_list)

my_list = [' ', 'O', ' ']
my_list = shuffle_list (my_list)
guess = player_guess ()
check_guess (my_list, guess)

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# Functions in Python is a block of code to carry out a specific task, will contain its own scope and is called by name.
# It s block of code that is also called by its name (independent).
# It can have different parameters or may not have any at all. If any data (parameters) are passed, they are passed explicitly.
# It may or may not return any data.
# It does not deal with Class and it's instance concept.
# It cannot alter the Object's state but it can operate on an Object.

# Syntax:
# def Function_Name (Arg1, Arg2, ...) :
#	......
#	Function Body
#	......
#       return expression

# Functions can be User-defined or In-Built or Anonymous.
# Anonymous functions use the keyword 'lambda' instead of 'def' for definition.

# Creating a function requires a very specific syntax, including the 'def' keyword, correct indentation and proper structure.
# The name of the function is all lowercases with underscores between words (Snake casing).
# Everything indented is considered to be inside of the function.
# The 'return' keyword can be used to send back the result of the function. It allows to assign the output of the function to a variable.
# They are used to create clean repeatable code for efficient programming.

# The number of parameters in the function call shall be equal to that in the function definition. Otherwise, it throws a "TypeError" error.
# To avoid this error, the variable is defined with a default value in the function definition.
# The Data-type of the parameters are not defined initially while defining. However, this feature can result into bugs that can be hard to find.

# Returning a Tuple from a function can cause error if there are not enough variables on LHS as there are elements in the Tuple returned.
# It is a safe method to capture the entire Tuple in a single variable and then split them by observing the number of elements present in the Tuple.
