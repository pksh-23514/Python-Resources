# Integer Data-type
val = 23
print ("DATA: ", val)
print ("TYPE: ", type (val))

# List Data-type
val = ['Prabhat', 'Kiran']
print ("DATA: ", val)
print ("TYPE: ", type (val))

# Float Data-type
val = 14.5
print ("DATA: ", val)
print ("TYPE: ", type (val))

# Boolean Data-type
val = True
print ("DATA: ", val)
val = False
print ("DATA: ", val)
print ("TYPE: ", type (val))

future_val = None
print ("DATA: ", future_val)
future_val = 23
print ("DATA: ", future_val)

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# The Type of Object assigned to a variable can be checked using Python's built-in "type()" function.
# Python uses Dynamic-typing, meaning the variable can be reassigned to a different Data Type. It differs from other languages that are Statically-typed.

# Briefly, the Data Types are:
# 1. Integers (int)         => Whole Numbers such as 300 etc.
# 2. Floating Point (float) => Numbers with a Decimal Point such as 2.3, 100.0 etc.
# 3. Strings (str)          => Ordered Sequence of Characters such as "hello" 'Prabhat' etc.
# 4. Lists (list)           => Ordered Sequence of Objects such as [10, "hello", 200.3] etc.
# 5. Dictionaries (dict)    => Unordered Key:Value pairs such as {"mykey":"value", "Name":"Prabhat"} etc.
# 6. Tuples (tup)           => Ordered Immutable Sequence of Objects such as (10, "hello", 200.3) etc.
# 7. Sets (set)             => Unordered Collection of Unique Objects such as {"a", "b"} etc.
# 8. Booleans (bool)        => Logical value indicating True or False only.

# The Operators involved in the Numbers are as follows:
# 1. Addition       => +
# 2. Subtraction    => -
# 3. Multiplication => *
# 4. Division       => /
# 5. Modulo         => %
# 6. Power          => **
# 7. Brackets       => ()

# The keyword "None" can be used as a Placeholder for any variable whose value is not determined at the time of initialization.
# However, it will be used later in the code and using the "None" keyword will avoid any "NameError:" error generation for the variable.

# Floating point numbers are represented in the Computer Hardware as Base-2 (binary).
# Unfortunately, most of the decimal fractions cannot be represented exactly as binary fractions.
# Generally, the decimal floating-point numbers entered are only approximated by the binary floating-point numbers actually stored in the machine.
# For eg.- Consider the decimal fraction 1/3. It can be approximated in Base-10 as: 0.33333333... but it will never be exactly 1/3.
# Similarly, no matter how many Base-2 digits are used; the binary fraction can never exactly match the represented number.
# For eg.- Consider the decimal fraction 0.1. It can be approximated in Base-2 as: 0.0001100110011001100110011001100110011001100110011... but never matches 0.1.
# This is called the Representation error. This is the chief reason why Python won't often display the exact decimal number as expected in an expression.
# For eg.- 0.1+0.2 => 0.30000000000000004
# The IEEE-754 floating point arithmetic standard is used to represent the floating point numbers.
# It decides the floating point accuracy and machine's abilities to represent numbers in memory.
