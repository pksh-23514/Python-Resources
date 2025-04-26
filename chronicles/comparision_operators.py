print (2 == 2)
print (3 == '3')
print ("hello" == "bye")
print ({1, 2, 3} == {1, 3, 2})
print (0 == False)

print ('2' != 2)
print ("hello" != "Hello")
print ([1, 2] != [2, 1])

print (4 < 1)
print (3 < 3)
print ('Ayushi' < 'ayushi')
print (0.9999999 < True)
print ([0] < [False])
print ((1, 2, 3) < (1, 2, 3, 4))
print ((1, 3, 2) < (1, 2, 3))
print (() < (0,))
print ((1, 'one') < (2, 'two'))
print ({1, 2, 3} < {1, 3, 2})

print (5 > 23)
print (0.5 > False)
print (3, 4, 5 > 3,4, 5.0)
print (type ((3, 4, 5 > 3,4, 5.0)))
print ((3, 4, 5) > (3, 4, 5.0))

print ("bye" >= 'Bye')
from math import pi
print (3.14 >= pi)
print (1 <= 0)
print ("hello" <= 'hi')

print (2.0 != 2)
print (4**0.5 == 2)
print (3 < 3.0)

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# The Comparision or Relational operators are used to compare 2 variables with values.
# The Comparison operators include the following:
# Equal to - ==
# Not equal to - !=
# Greater than - >
# Less than - <
# Greater than or equal to - >=
# Less than or equal to - <=

# Comparision operators works well on Containers like Set, List, Tuple or String. However, if the values are of different types, they can't be compared.
# Eg.- (1, 2) < ('One', 'Two') => TypeError: ‘<‘ not supported between instances of ‘int’ and ‘str’
# But if there are values of same type at the same indices, then it can be compared.
# Eg.- (1, 'one') < (2, 'two') => True
# Eg.- (1, 'one') < ('two', 2) => TypeError: ‘<‘ not supported between instances of ‘int’ and ‘str’
# Value (1) is equal to (True) and (0) is equal to (False).
# Comparision between the Dictionary type is not allowed.
# Eg.- {1 : 'one', 2 : 'two'} < {1 : 'three', 2 : 'four'} => TypeError: ‘<‘ not supported between instances of ‘dict’ and ‘dict’
# Comparision between the Sets type can have the same elements but at different indices as it is an Unordered sequence.
# Eg.- print ({1, 2, 3} == {1, 3, 2}) => True

# Comparision without the placeholders is like individual comparision and not Container comparision.
# Eg.- 3, 4, 5 > 3, 4, 5.0 => (3, 4, True, 4, 5.0)
#      A Tuple is created instead of the comparision between all the elements on LHS and RHS. The value 'True' is the result of (5 > 3).
# Even if the placeholder is put on one side, the desired comparision will not take place.
# Eg.- 3, 4, 5 > (3, 4, 5.0) => TypeError: ‘>’ not supported between instances of ‘int’ and ‘tuple’

# In Python, the value and it's decimal form is equal.
# Eg. - The integer 3 and the floating-point number 3.0 clearly have the same value, so if (3 == 3.0) is true.
