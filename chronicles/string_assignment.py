# Single Quotes String Data-type
val = 'Hello World!'
print ("DATA: ", val)
print ("LENGTH: ", len (val))
print ("TYPE: ", type (val))

# Double Quotes String Data-type
val = "Hello World!"
print ("DATA: ", val)
print ("LENGTH: ", len (val))
print ("TYPE: ", type (val))

# Mixture of Single and Double Quotes String Data-type
val = "Single quotes can't print it!"
print ("DATA: ", val)
print ("LENGTH: ", len (val))
print ("TYPE: ", type (val))

# Mixture of Single and Double Quotes String Data-type
val = 'Double quotes "cannot" print it!'
print ("DATA: ", val)
print ("LENGTH: ", len (val))
print ("TYPE: ", type (val))

# String Indexing
val = "Hello World"
ch = val [3]
print ("CHARACTER using Indexing: ", ch)
ch = val [-3]
print ("CHARACTER using Reverse Indexing: ", ch)

# String Slicing
val = "Hello World"
sub = val [6:]
print ("SLICE: ", sub)
sub = val [:5]
print ("SLICE: ", sub)
sub = val [3:8:1]
print ("SLICE: ", sub)
sub = val [3:8]
print ("SLICE: ", sub)
sub = val [::]
print ("SLICE: ", sub)
sub = val [::2]
print ("SLICE: ", sub)
sub = val [3:8:2]
print ("SLICE: ", sub)
sub = val [::-1]
print ("SLICE: ", sub)

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# Where the Single quote appears as a part of the string, we use Double quotes to initialize the string.
# Strings are a sequence, which means Python can use index to call parts of the sequence. In Python, we use brackets [] after an object to call its Index.
# We should also note that indexing starts at "0" for Python.
# Negative indexing is also allowed in Python and "-1" is the index for the last character.
# Character:       H  e  l  l  o
# Index:           0  1  2  3  4
# Reverse Index:   0 -4 -3 -2 -1
# You can use the "len()" function to check the length of a String.

# Slicing allows to grab a sub-section of multiple characters i.e. a "slice" of the String.
# Syntax for Slicing: [start:stop:step]
# Where: 'start' - numerical index for the slice start. 'stop' - the index the slice will go upto (but not include). 'step' - size of the jump.
# 'start' is inclusive of that index position but 'stop' is exclusive of that index position (i.e. upto that index but not including that index).
# The notation "[::]" will include the complete String as the default 'step' has a value of 1. 
# The clever way to reverse a String is to go from the start to the end index but with a 'step' of -1.

# The Escape Sequences are used to format the way in which the String can be printed.
# Popular Escape Sequences are: \n, \t, \\, \' and \".
