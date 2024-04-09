def my_func (*args):
    print (args)
    print (type (args))
my_func (10, 20, 30, 40, 50)

def my_func (*num):
    print (num)
    print (type (num))
my_func (10, 20, 30, 40, 50)
print ("")

def my_func (*args):
    for item in args:
        print (item)
    print ("")
my_func (5, 14, 23)

def my_func (arg1, *args):
    print("First argument :", arg1)
    for item in args:
        print ("Next argument through *args :", item)
    print ("")
my_func ('Hello', 'Welcome', 'to', 'Python')

def my_func (**kwargs):
    print (kwargs)
    print (type (kwargs))
    print ("")
my_func (first=10, second=20, third=30)

def my_func (**kwargs):
    if 'fruit' in kwargs:
        print (f"The choice of fruit is {kwargs ['fruit']}.")
    else:
        print (f"The choice of vegetable is {kwargs ['vegetable']}.")
    print ("")
my_func (fruit='grapes', vegetable='potato', nuts='cashew')

def my_func (arg1, **kwargs):
    print("First argument :", arg1)
    for (key, value) in kwargs.items ():
        print (f"{key} => {value}")
    print ("")
my_func ("Hi", start='How', mid='are', end='you')

def my_func (arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
args = ("How", "are", "You")
my_func (*args)
kwargs = {'arg1' : 'How', 'arg2' : 'are', 'arg3' : 'you'}
my_func (**kwargs)
print ("")

def my_func (*args, **kwargs):
    print("args: ", args [0])
    print("kwargs: ", kwargs ['mid'])
my_func ('How', 'are', 'You', first="Where", mid="are", last="You")

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# There are 2 special symbols used for passing Arguments: *args (Non-Keyword Arguments) and **kwargs (Keyword Arguments)
# The characters (* and **) used in the notations "*args" or "**kwargs" is required when there is uncertainty about the number of arguments to be passed in a function.

# The special syntax "*args" in function definitions is used to pass a variable number of arguments to a function.
# It is used to pass a non-keyworded, variable-length argument list.
# Syntax (by convention but not mandatory): *args
# With "*args", any number of extra arguments can be tacked on to the formal arguments that are previously defined.
# Using the (*), the variable that is associated with the (*) becomes iterable.

# The special syntax "**kwargs" in function definitions is used to pass a keyworded, variable-length argument list.
# The (**) allows to pass through any number of keyword arguments to the function.
# A keyword argument is an argument provided with a name to the variable as it is passed to the function.
# It can be thought of as a Dictionary that maps each keyword to the value passed alongside with it.
# This is the reason the "**kwargs" are not printed in any specific order when they are iterated.

# Note: *args receives arguments as a tuple and **kwargs receives arguments as a dictionary.

# If both the "*args" and "**kwargs" are used in the function definition, the order in which they are passed shall be same as written in the definition.
# If the positions of "*args" or "**kwargs" are jumbled while passing them to the function, it throws a "SyntaxError" error.
