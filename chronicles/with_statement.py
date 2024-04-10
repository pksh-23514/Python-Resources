path = r"../data/sample_with_Read.txt"
with open (path, 'rt') as my_file:
    contents = my_file.read ()
print (contents, end='')
print ("=========================================================")

path = r"../data/sample_with_Write.txt"
with open (path, 'wt') as my_file:
    my_file.write ("Hello World!\n")
print ("Writing the file...")
with open (path, 'rt') as my_file:
    contents = my_file.read ()
print (contents, end='')
print ("=========================================================")

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# The 'with' statement is used for resource management and exception handling. It is mostly used with the file streams, locks, sockets, subprocesses and telnets etc.
# There is no need for a file to be closed manually in the 'with' statement as the statement itself ensures proper acquisition and release of resources.
# It reduces the size of the code, therefore making it compact and readable. The proper resource management helps in avoiding bugs and leaks.
