my_list = ["Hello", ",", "How", "are", "you", "?"]
for item in my_list:
    print (f"{item} ", end='')
print ("\n")

my_dict = {'k1' : "23", 'k2' : "14", 'k3' : "05"}
for key in my_dict:
    print (f"{key} -> {my_dict [key]}")
print ("")

my_str = "Sunflower"
for ch in my_str:
    print (f"{ch}", end='')
print ("\n")

my_tuple = (14, 23, 5)
for item in my_tuple:
    print (f"{item} ", end='')
print ("\n")

my_set = {13, 'thirteen', "XIII"}
for item in my_set:
    print (f"{item} ", end='')
print ("\n")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in my_list:
    if ((num % 2) == 1):
        print (f"Odd Number:  {num}")
    else:
        print (f"Even Number: {num}")
print ("")

my_sum = 0
for num in my_list:
    my_sum = my_sum + num
    print (f"Current: {my_sum}")
print (f"Sum: {my_sum}\n")

for _ in 'Hey':
    print ("Coldstone")
print ("")

my_tuple = ((1, 2), (2, 3), (3, 4), (4, 5))
for item in my_tuple:
    print (item)
for (a, b) in my_tuple:
    print (f"{a} {b}")
print ("")

my_dict = {'k1' : "23", 'k2' : "14", 'k3' : "05"}
print (my_dict.items ())
for (key, values) in my_dict.items ():
    print (values)
print ("")

for i in range (0, 5, 1):
    for j in range (0, (i + 1), 1):
        print ("*", end='')
    print ("")
print ("")

for i in range (1, 6, 1):
    print (i)
else:
    print ("count is greater than 5!")

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# The 'for' loop is used for the sequential traversal. They are used to implement only the collection-based iteration.
# The 'for' loop Syntax is:
# =========================
# for iterator_var in sequence/iterable:
    # statements to be executed repeatedly
# statements outside of the for-loop as the indentation has been removed

# The 'iterable' means the Object can be iterated over. It is used for iterating over an iterable like Strings, Tuples, Lists, Sets or Dictionaries.
# The loop assigns each item in the List to the iterator variable and continues till all the items in the List have been processed.
# The loop assigns each key of the Dictionary to the iterator variable and continues till all the Keys in the Dictionary have been processed.
# The loop assigns each character of the String to the iterator variable and continues till all the characters in the String have been processed.
# The loop assigns each item in the Tuple to the iterator variable and continues till all the iterms in the Tuple have been processed.
# The loop assigns each item in the Set to the iterator variable and continues till all the items in the Set have been processed.

# If iteratation occurs without utilizing the iterator variable, the '_' underscore can be used instead of a variable name.
# A single '_' underscore is a conventional way to indicate unused variables when the loop variable is not getting utilized anywhere.

# The Tuple of Tuples or List of Tuples can be iterated using a 'for' loop by utilizing the feature of Tuples Unpacking.
# This method is also useful in case of iterating through the Dictionaries by utilizing the "items()" method.
# The "items()" method returns a key-value pair in form of Tuples in a List.

# Nested 'for' loops means 'for' loops under 'for' loops.
# The Nested 'for' loop Syntax is:
# ================================
# for iterator_var in sequence/iterable:
    # for iterator_var in sequence/iterable:
        # statements to be executed inside the Inner loop
    # statements to be executed inside the Outer loop
# statements outside of the Nested loop as the indentation has been removed

# The 'else' statement in 'for' loop can be executed only after the condition becomes FALSE.
# If the loop is broken or if an Exception is raised, the Else statements will not be executed.
# The 'for-else' loop Syntax is:
# ==============================
# for iterator_var in sequence/iterable:
    # statements to be executed repeatedly
# else:
    # statements to be executed after the loop is terminated naturally.
