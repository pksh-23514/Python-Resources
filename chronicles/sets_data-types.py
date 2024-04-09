my_set = {'one', 2, 3.0}
print ("DATA: ", my_set)

my_list = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4]
my_set = set (my_list)
print ("DATA: ", my_set)

my_set = {1, 2, 3}
print ("DATA: ", my_set)
print ("LENGTH: ", len (my_set))
my_set.add (4)
print ("DATA: ", my_set)
print ("LENGTH: ", len (my_set))
my_set.add (2)
print ("DATA: ", my_set)
print ("LENGTH: ", len (my_set))
my_set.add (True)
print ("DATA: ", my_set)
print ("LENGTH: ", len (my_set))

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# Sets are unordered collection of unique elements i.e. they do not allow duplicate values. They are built-in Data Types.
# They cannot be sorted, indexed or sliced.
# It uses '{}' brackets and ',' commas to separate the Objects present in the Sets.
# They are Immutable i.e. once the element is assigned inside a Set, it cannot be changed. However, elements can be added or removed in the Sets.
# The "set()" function can be used to create a new Set.
# It is very useful to pick the unique elements from a pile of duplicate elements List using the "set()" function.
# The "len()" function can be used to find the Length of the Sets.

# The "add()" method can be used to add a new element to the Sets. However, it will not add the element if it is already existing the in the Set.
# Note: The values (True, 1) and (False, 0) are considered the same value in sets and are treated as duplicates.

