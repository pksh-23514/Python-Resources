print ((1 < 2) and (2 < 3))
print (('h' == 'he') and (4 < 5))
print ((1 < 2) or (2 < 3))
print (('h' == 'he') or (4 < 5))
print ((1 == 2) or (2 == 3))
print (not (2 == 2))
print (not ('h' != 'h'))

x = 5
y = 10

if ((x > 0) and (y < 20)):
    print ("Both the conditions are True.")
else:
    print ("Either one or both the conditions are False.")

if ((x == 4) or (y < 15)):
    print ("At least one of the conditions is True.")
else:
    print ("Both the conditions are False.")

is_True = True
if (not is_True):
    print ("The value is False.")
else:
    print ("The value is True.")

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# The Logical operators are used to combine the Conditional statements.
# The Logical operators include the following:
# and - Returns TRUE if both the statements are true.
# or  - Returns TRUE if one of the statements is true.
# not - Returns TRUE if the statement is false.
