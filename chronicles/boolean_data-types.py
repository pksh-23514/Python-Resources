my_bool = True
print ("VALUE: ", my_bool)
my_bool = False
print ("VALUE: ", my_bool)

print ("VALUE: ", (1 > 2))
print ("VALUE: ", (1 == 1))

print ("VALUE: ", bool ("abc"))
print ("VALUE: ", bool (""))
print ("VALUE: ", bool (23))
print ("VALUE: ", bool (0))
print ("VALUE: ", bool (["apple", "cherry", "banana"]))
print ("VALUE: ", bool ([]))

print ("VALUE: ", bool (False))
print ("VALUE: ", bool (None))
print ("VALUE: ", bool (()))
print ("VALUE: ", bool ({}))

a = 23
print ("TYPE: ", type (a))
my_bool = bool (a)
print ("VALUE: ", my_bool)
print ("TYPE: ", type (my_bool))

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# Booleans are operators that conveys 'True' or 'False' logic to a particular statement. They are used in the Control Flow Logic.
# The expression involving the comparision of two values will return a Boolean value always.
# The "bool()" function can be used to return a Boolean value and can also be used to cast a variable to Boolean Data Type.
# There are a lot of Built-in methods that return a Boolean value. Eg.- isinstance()

# Almost any value is evaluated to 'True' if it has some sort of content.
# Any String is 'True', except empty Strings.
# Any Integer is 'True', except 0.
# Any List, Tuple, Set and Dictionary are True, except empty ones.
