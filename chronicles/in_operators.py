val = 'x' in [1, 2, 'x']
print (val)
print (type (val), end='\n\n')

val = 'x' in [1, 2, 3]
print (val)
print (type (val), end='\n\n')

val = 'a' in "Apple"
print (val, end='\n\n')

val = 'k2' in {'k1' : 23, 'k2' : 14}
print (val)
val = 5 in {'k1' : 23, 'k2' : 14}.values ()
print (val, end='\n\n')

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# Membership Operators are
# The "in" keyword can be used to check if a value is present in a sequence (List, Range, String etc.) and return a Boolean value.
# They are very useful for a quick check on Strings.
