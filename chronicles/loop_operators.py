for num in range (10):
    print (f"{num} ", end='')
print ("\n")

for num in range (1, 10, 2):
    print (f"{num} ", end='')
print ("\n")

for num in range (9, -1, -1):
    print (f"{num} ", end='')
print ("\n")

print (range (0, 10, 2))
print (list (range (0, 10, 1)))
print ("")

val = range (10)[0]
print ("VALUE: ", val)
val = range (10)[-1]
print ("VALUE: ", val)
print ("")

my_list = ["apple", "banana", "cherry", "date"]
for i in range (len (my_list)):
    print (my_list [i])
print ("")

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# The "range()" function can be used to generate and return a sequence of numbers.
# Syntax: range (start, stop, step)
# Where: 'start' is by default set to 0 and is optional. 'stop' is the limit excluding itself and is mandatory. 'step' is by default set to increment of 1 and is optional.
# The "range()" cannot be directly printed outside of the loop. It has to be converted to a List and then printed.
# It does not accept any Float values i.e. the argument cannot be a floating-point number or non-integer number. Eg. - range (3.3) is not allowed.
# If the argument is anything other than integer numbers, it will generate a "TypeError" error.
# This function generates a sequence of numbers and they can be accessed using an index value. Both positive and negative indexing is possible.
# The List can be traversed using the "range()" function by generating the Indices from 0 to (len-1) as sequence and accessing the elements of the List.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

my_str = "Python"
for item in enumerate (my_str):
    print (item)
    print (type (item))
print (type (enumerate (my_str)))
print (list (enumerate (my_str)))
print ("")

for item in enumerate (my_str, 100):
    print (item)
print ("")

for (index, letter) in enumerate (my_str):
    print (f"Index: {index} => Letter: {letter}")
print ("")

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# The "enumerate()" function can be used to add a counter as the Key to an iterable and returns it in the form of an Enumerating Object.
# Syntax: enumerate (iterable, start)
# Where: 'iterable' is the Object that supports iteration and is mandatory. 'start' is the starting Key value and is by default set to 0 and is optional.
# The Enumerated Object can be converted into a List of Tuples by using the List Constructor.
# The Key can be started with any arbitary values by initializing the 'start' argument.
# Using Tuples Unpacking, the output can be split into the Key and Value separately.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

my_index = [1, 2, 3]
my_value = ['a', 'b', 'c']
my_str = ["Apple", "Ball", "Cat"]
print (zip (my_index, my_value, my_str))
print ("")
for item in zip (my_index, my_value, my_str):
    print (item)
    print (type (item))
print ("")

my_index = [1, 2, 3, 4, 5, 6]
my_value = ['a', 'b', 'c']
my_str = ["Apple", "Ball", "Cat", "Dog"]
for item in zip (my_index, my_value, my_str):
    print (item)
print ("")

my_index = [1, 2, 3]
my_value = ['a', 'b', 'c']
print (list (zip (my_index, my_value)))
print ("")

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
print (set (zip (name, roll_no)))
print ("")

stocks = ["RIL", "ITC", "VBL"]
prices = ["3000", "500", "1500"]
my_dict = dict (zip (stocks, prices))
print (my_dict)
print ("")

names = ['Mukesh', 'Rohini', 'Krishna']
ages = [24, 50, 18]
for (i, (name, age)) in enumerate (zip (names, ages)):
    print(i, name, age)
print ("")

names = ['Mukesh', 'Rohini', 'Krishna']
ages = [24, 50, 18]
emp_nos = [4, 1, 3, 2]
mapped = list (zip (names, ages, emp_nos))
print ("Zipped: ", mapped)
name, age, emp_no = zip (*mapped)
print ("Unzipping...")
print ("Names: ", name)
print ("Ages: ", age)
print ("Emp. No.: ", emp_no)

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# The "zip()" function can be used to zip all the iterable containers into a single iterator Object containing the mapped values from all the Containers.
# Syntax: zip (iterable_containers)
# Where: 'iterable_containers' are the multiple iterable containers such as List, String, Tuples, Dictionary etc.
# The direct use of the "zip()" function will return a Memory location where the Zip is waiting to be generated.
# If the given iterable containers are of different lengths, the resultant single iterator Object has the length equal to the smallest iterable container passed.
# The single iterator Object can be converted into a List of Tuples using the List Constructor.
# The single iterator Object can be converted into a Set of Tuples using the Set Constructor.
# The single iterator Object can be converted into a Dictionary of Tuples using the Dictionary Constructor. However, not applicable for more than 2 containers.
# The combination of "zip()" and "enumerate()" can be used to process multiple Lists or Tuples and also access their indices.
# Unzipping means to convert the zipped values back to the individual sequence in form of Tuples.
# Syntax: zip (*iterator_object)
# Where: 'iterator_object' is the single iterator Object containing the mapped values from all the Containers.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
