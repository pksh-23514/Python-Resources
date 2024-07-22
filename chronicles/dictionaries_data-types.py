my_dict = {'key1' : 'value1', 'key2' : 'value2'}
print ("DATA: ", my_dict)
print ("LENGTH: ", len (my_dict))
print ("VALUE: ", my_dict ['key1'])

my_dict = {'k1' : 23, 'k2': [0, 1, 2], 'k3' : 14.5, 'k4' : {'key' : 5}}
print ("VALUE: ", my_dict ['k2'])
print ("VALUE: ", my_dict ['k4'])
print ("VALUE: ", my_dict ['k4']['key'])

my_dict = dict (k1 = 100, k2 = '200')
print ("DATA: ", my_dict)
print ("LENGTH: ", len (my_dict))
my_dict ['k3'] = 300
print ("DATA: ", my_dict)
print ("LENGTH: ", len (my_dict))
my_dict ['k2'] = 200
print ("DATA: ", my_dict)

my_dict = {"brand" : "Ford", "model" : "Mustang", "year" : 1964, "year" : 2020}
print ("DATA: ", my_dict)
print ("LENGTH: ", len (my_dict))

my_dict = {"brand" : "Ford", "model" : "Mustang", "year" : 1964}
key = my_dict.keys ()
values = my_dict.values ()
pairs = my_dict.items ()
my_dict ["color"] = "blue"
print ("KEYS: ", key)
print ("VALUES: ", values)
print ("PAIRS: ", pairs)
out = my_dict.pop ('year', 2024)
print ("DATA: ", my_dict)
print ("VALUES: ", out)

my_dict = {1.1 : "Hi", 2.3 : "Hello", 5 : "How are you?"}
for item in my_dict.items():
    print (item)

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# Dictionaries are unordered mappings for storing objects. They use a key-value pairing to store the Objects. They are built-in Data Types.
# It uses '{}' brackets and ',' commas to separate the Objects present in the Dictionary. It uses ':' colon to separate the Key and Value pair.
# The key-value pair can be used to quickly grab objects without needing to know the index position of the value.
# Syntax: {'key1':'value1', 'key2':'value2'}
# The key can be any immutable Object (integer, float, character, Strings etc.).
# The values can be of any Data Type.
# The "dict()" function can be used to create a new Dictionary.
# The "len()" function can be used to find the number of key-value pairs present in the Dictionaries.
# The Nested Dictionaries can be accessed using multiple Key values.

# They cannot be sorted, indexed or sliced.
# The key-value pair can be changed, added or removed after the Dictionaries are created.

# Since, each key-value pair is unique combination; Dictionaries do not allow duplicate values. It will overwrite the existing value for the Key.

# The "keys()" method can be used to return the Key values (view object) present in the Dictionaries. It will reflect all the changes made to the Dictionaries.
# The "values()" method can be used to return the Values (view object) present in the Dicrtionaries. It will reflect all the changes made to the Dictionaries.
# The "items()" method can be used to return the key-value pair (view object) in the form of Tuples. It will reflect all the changes made to the Dictionaries.
# The "pop()" method can be used to remove the Value based on the Key passed. The method returns the value of the removed item or default value specified or an error.
