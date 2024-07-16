my_list = [1, 2, 3]
print ("DATA: ", my_list)

my_list = ['STRING', 100, 23.5, True]
print ("DATA: ", my_list)
print ("LENGTH: ", len (my_list))
print ("VALUE: ", my_list [0])
print ("VALUE: ", my_list [-1])
print ("SLICE: ", my_list [1:3:1])

list1 = ['Hello', 'World']
list2 = ['!']
print ("NEW: ", list1 + list2)

my_list = ['STRING', 100, 23.5, True]
my_list [1] = 14
print ("DATA: ", my_list)

my_list = [1, 2, 3, [4, 5, 6]]
print ("VALUE: ", my_list [0])
print ("VALUE: ", my_list [2])
print ("VALUE: ", my_list [3])
print ("VALUE: ", my_list [3][0])
print ("VALUE: ", my_list [3][2])

my_str = "ABCDE"
my_tuple = ('A', 'B', 'C', 'D', 'E')
my_sets = {'A', 'B', 'C', 'D', 'E'}
my_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
print ("STRING TO LIST     : ", list (my_str))
print ("TUPLES TO LIST     : ", list (my_tuple))
print ("SETS TO LIST       : ", list (my_sets))
print ("DICTIONARY TO LIST : ", list (my_dict))

my_list = [1, 2, 3]
print ("DATA: ", my_list)
list_type = type (my_list.append (4))
print ("DATA: ", my_list)
print ("TYPE: ", list_type)
out = my_list.pop ()
print ("DATA: ", my_list)
print ("VALUE: ", out)
list_type = type (my_list.insert (3, 4))
print ("DATA: ", my_list)
print ("TYPE: ", list_type)
list_type = type (my_list.insert (3, 4))
print ("DATA: ", my_list)
print ("TYPE: ", list_type)
out = my_list.remove (4)
print ("DATA: ", my_list)
print ("VALUE: ", out)

my_list = ['Ford', 'Mitsubishi', 'BMW', 'VW']
print ("DATA: ", my_list)
list_type = type (my_list.sort ())
print ("DATA: ", my_list)
print ("TYPE: ", list_type)
list_type = type (my_list.sort (reverse=True))
print ("DATA: ", my_list)
print ("TYPE: ", list_type)
list_type = type (my_list.sort (key=len))
print ("DATA: ", my_list)
print ("TYPE: ", list_type)

my_list = [1, 2, 3]
print ("DATA: ", my_list)
list_type = type (my_list.reverse ())
print ("DATA: ", my_list)
print ("TYPE: ", list_type)

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# Lists are ordered sequences that can hold a variety of Object types. They are built-in Data Types.
# It uses '[]' brackets and ',' commas to separate the Objects present in the List.
# They support indexing and slicing. They can also be nested and have a variety of methods that can be called off of them.
# They allow duplicate values to be stored inside them.
# Most of the methods are 'In-Place' methods i.e. they operate on the input List itself without creating another List or returning a new modified List.
# The "len()" function can be used to find the Length of the List.

# The "list()" function can be used to create a new List.
# Syntax: list (iterable)
# Where: iterable - Object that can be a sequence (string/tuples) or collection (sets/dictionary) or any iterator.
# If no parameter is passed, the function will return a List with 0 elements.

# Indexing of the List starts with the index '0'. Negative indexing is allowed for the List.
# Lists can be mutated by assigning a new value to any index position of the List.

# Slicing of the List can be done using the format: [start, stop, step]

# The '+' operator can be used to Concatenate the Lists.

# The "append()" method can be used to add a new element to the end of the List. It is an In-Place method which doesn't return a new List after appending.
# The "insert()" method can be used to add a new element to the particular index of the List. It is an In-Place method which doesn't return a new List after inserting.
# The "pop()' method can be used to pop out an element from any index of the List and returns the popped value. The default index is the end of the List.
# The "remove()" method can be used to delete the first occurence of the element in the List. It does not returns the removed value.

# The "sort()" method can be used to sort the List based on the type of ordering and the sorting criteria. The default order is Ascending and it doesn't return any value.
# The sorting criteria shall be a function that returns a value based on which the sorting is done.
# The "sort()" method is an In-place method which will sort the List in-place without returning a new List after sorting.

# The "reverse()" method can be used to reverse the List. It is an In-Place method which doesn't return a new List after reversing.
