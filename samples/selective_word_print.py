# Write a program that takes a String and prints out the statement containing the words that start with the character 's' only.
# I/P: Print only the words that start with s in this sentence
# O/P: start s sentence

"""
**************************************************************
**************************************************************
"""

my_str = "Print only the words that start with s in this sentence"
my_list = my_str.split ()
res = list ()

for item in my_list:
    if (item [0] == 's'):
        res.append (item)

result = " ".join (res)
print (result)
