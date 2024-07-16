my_tuples = (1, 'two', 3.0)
print ("DATA: ", my_tuples)
print ("VALUE: ", my_tuples [0])
print ("VALUE: ", my_tuples [-1])
print ("LIST: ", my_tuples [1:])
print ("LENGTH: ", len (my_tuples))

my_str = "ABCDE"
my_tuple = ('A', 'B', 'C', 'D', 'E')
my_set = {'A', 'B', 'C', 'D', 'E'}
my_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
print ("STRING TO TUPLE           : ", tuple (my_str))
print ("TUPLE TO TUPLE            : ", tuple (my_tuple))
print ("SET TO TUPLE              : ", tuple (my_set))
print ("DICTIONARY TO TUPLE       : ", tuple (my_dict))
print ("DICTIONARY ITEMS TO TUPLE : ", tuple (my_dict.items ()))

my_tuples = (1, 2, 3, 1)
print ("COUNT: ", my_tuples.count (1))
print ("INDEX: ", my_tuples.index (1))

my_tuples = ("apple",)
print (type (my_tuples))
my_tuples = ("apple")
print (type (my_tuples))

my_tuples = ("NITR", 500000, 'Engineering')
(college, fees, stream) = my_tuples
print (college)
print (fees)
print (stream)

my_tuples = (1, 2.0, 'three', "IV", 'five', 6.0, 7)
(first, *middle, last) = my_tuples
print (first)
print (middle)
print (last)
(first, middle, *last) = my_tuples
print (first)
print (middle)
print (last)
(*first, middle, last) = my_tuples
print (first)
print (middle)
print (last)

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# Tuples are similar to Lists. However, they are Immutable i.e. once the element is assigned inside a Tuple, it cannot be changed. They are built-in Data Types.
# Tuples use '()' paranthesis and ',' commas to separate the Objects present in the Tuples. They can hold a variety of Object types.
# They are ordered sequence and allow duplicate values inside them.
# They are used to implement Data Integrity while passing the Objects in the program.
# The "len()" function can be used to find the Length of the Tuples.

# The "tuple()" function can be used to create a new Tuple.
# Syntax: tuple (iterable)
# Where: iterable - Object that can be a sequence (string/tuples) or collection (sets/dictionary) or any iterator.
# If no parameter is passed, the function will return a Tuple with 0 elements.

# Indexing of the Tuples starts with the index '0'. Negative indexing is allowed for the Tuples.

# Slicing of the Tuples can be done using the format: [start, stop, step]

# The "count()" method can be used to count the number of occurences of the specified value in the Tuples.
# The "index()" method can be used to search for the first occurence of the specified value in the Tuples.

# To create a tuple with only one item, a ',' comma shall be added after the item or else the Python will not recognize it as a Tuple.

# Tuples Unpacking is a very powerful Tuple assignment feature that assigns the right-hand side of values into the left-hand side.
# In another way, it is called unpacking of a Tuple of values into a Variable.
# In packing, we put values into a new tuple while in unpacking we extract those values into a single variable.
# Note: In unpacking of Tuple, the number of Variables on left-hand side should be equal to number of values in given Tuple.

# There is a special syntax to pass optional arguments (*args) for Tuples Unpacking i.e. any number of arguments can be accomodated in place of (*args).
