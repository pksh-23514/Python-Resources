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

my_list = [1, 2, 3]
print ("DATA: ", my_list)
my_list.append (4)
print ("DATA: ", my_list)
out = my_list.pop ()
print ("DATA: ", my_list)
print ("VALUE: ", out)
my_list.insert (3, 4)
print ("DATA: ", my_list)
my_list.insert (3, 4)
print ("DATA: ", my_list)
out = my_list.remove (4)
print ("DATA: ", my_list)
print ("VALUE: ", out)

my_list = ['Ford', 'Mitsubishi', 'BMW', 'VW']
print ("DATA: ", my_list)
my_list.sort ()
print ("DATA: ", my_list)
my_list.sort (reverse=True)
print ("DATA: ", my_list)
my_list.sort (key=len)
print ("DATA: ", my_list)

my_list = [1, 2, 3]
print ("DATA: ", my_list)
my_list.reverse ()
print ("DATA: ", my_list)

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
# Most of the methods are 'in-place' methods i.e. they operate on the input List itself without creating another List or returning a new modified List.
# The "list()" function can be used to create a new List.
# The "len()" function can be used to find the Length of the List.

# Indexing of the List starts with the index '0'. Negative indexing is allowed for the List.
# Lists can be mutated by assigning a new value to any index position of the List.

# Slicing of the List can be done using the format: [start, stop, step]

# The '+' operator can be used to Concatenate the Lists.

# The "append()" method can be used to add a new element to the end of the List.
# The "insert()" method can be used to add a new element to the particular index of the List.
# The "pop()' method can be used to pop out an element from any index of the List and returns the popped value. The default index is the end of the List.
# The "remove()" method can be used to delete the first occurence of the element in the List. It does not returns the removed value.

# The "sort()" method can be used to sort the List based on the type of ordering and the sorting criteria. The default order is Ascending and it doesn't return any value.
# The sorting criteria shall be a function that returns a value based on which the sorting is done.

# The "reverse()" method can be used to reverse the List.
