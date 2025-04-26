name = "Sam"
last = name [1:]
new = 'P' + last
print ("VALUE: ", new)

str1 = "Hello "
str2 = "World "
str3 = "!"
val = str1 + str2 + str3
print ("VALUE: ", val)

ch = 'z'
val = ch * 10
print ("VALUE: ", val)

x = 2
y = 3
val = x + y
print ("VALUE: ", val)
x = '2'
y = '3'
val = x + y
print ("VALUE: ", val)

val = "Hello World"
new = val.upper ()
print ("VALUE: ", new)
new = val.lower ()
print ("VALUE: ", new)
new = val.split ()
print ("VALUE: ", new)
new = val.split ('o')
print ("VALUE: ", new)

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# Immutablility is the property of Strings i.e. direct substitution of a character from the String is not allowed.
# For eg.- To change the String "Sam" to "Pam", it cannot be executed using a simple replacement of a character from the String.
# name = "Sam"
# name [0] = 'P'
# TypeError: 'str' object does not support item assignment

# Concatenation of two or more Strings can be done by the '+' operator.

# Multiple Concatenation of the same String can be done by the '*' operator.

# String methods are in-built methods that operate on the given String.
# All the String methods returns new values. They do not change the original String.
# The String methods are listed here: https://www.w3schools.com/python/python_ref_string.asp
