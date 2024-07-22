num = [12, 13, 14]
double = [(x * 2)  for x in num]
print (double)
print (type (double))
square = [(x ** 2) for x in num]
print (square)
print (type (square))
print ("")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
my_list = [(item) for item in fruits if "a" in item]
print (my_list)
print ("")

my_list = [(i) for i in range (10) if ((i % 2) == 0)]
print (my_list)
print ("")

my_str = "Hello"
my_list = [(letter) for letter in my_str]
print (my_list)
print ("")

my_list = [(x * y) for x in [2, 4, 6] for y in [1, 10, 100]]
print (my_list)
print ("")

my_list = [[y for y in range (5)] for x in range (3)]
print (my_list)
print ("")

my_list = ["Even" if ((num % 2) == 0)
        else "Odd" for num in range (10)]
print (my_list)
print ("")

my_list = [num for num in range (100)
        if ((num % 3) == 0) if ((num % 10) == 0)]
print (my_list)
print ("")

name = ["apple", "banana", "cherry", "orange"]
value = [23, 14, 41, 23]
my_tuple = [(name, value) for (name, value) in zip (name, value)]
print (my_tuple)

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# The List Comprehensions can be used as a short form syntax to create a new List based on an existing List.
# It uses '[]' brackets containing the expression to be executed for the selected elements and For loop to iterate the List.
# Syntax: new_List = [expression(element) for element in iterable if condition]
# Where: 'expression' is the operation to be executed. 'element' is the value taken from the iterable. 'condition' is filter to choose the element to be passed.

# If there is a loop along with ".append()" to create a List based on a condition, they can be replaced with the List Comprehension.
# For Eg. - The below is choosing all the names of the fruits if they have the character 'a' in their name.
# for x in fruits:
#     if "a" in x:
#         newlist.append(x)

# Parallel selection of elements from various Lists can be written in a sequential manner for each of the List.

# Nested List Comprehensions is a List Comprehension within another List Comprehension. It is similar to the Nested For loop.
# The 'expression' itself then becomes a List Comprehension.

# The Nested If or If-Else statements can be used inside the List Comprehension for efficient List creation.

# The List of Tuples can be created from multiple Lists by zipping them into one iterator Object and using Tuples Unpacking in the 'expression'.
