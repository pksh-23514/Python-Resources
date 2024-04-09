path = r"../data/sample_Read.txt"
fp = open (path, 'rt')
print (fp.read (), end='')
print ("================================================================")
print (fp.read ())
print ("Empty print on the above line due to the EOF.")
print ("================================================================")
print ("Need to position the cursor at the beginning of the file.")
print ("================================================================")
fp.seek (0)
print (fp.read (), end='')
print ("================================================================")
fp.close ()

fp = open (path, 'rt')
print (fp.seek (5))
print (fp.seek (5, 0))
print (fp.read (11))
print ("================================================================")
fp.close ()

fp = open (path, 'rt')
print (fp.seek (0, 1))
print (fp.read (10))
print ("================================================================")
fp.close ()

fp = open (path, 'rt')
print (fp.seek (0, 2))
print (fp.read (10))
print ("================================================================")
fp.close ()

fp = open (path, 'rt')
print (fp.readline (), end='')
print ("================================================================")
fp.close ()

fp = open (path, 'rt')
lines = fp.readlines ()
print (f"Line-1: {lines [0]}Line-2: {lines [1]}Line-3: {lines [2]}", end='')
print ("================================================================")
fp.close ()

path = r"../data/sample_Write.txt"
fp = open (path, 'wt')
fp.write ("This is a newly created File.\n")
fp.write ("It is to test the write() method in Write mode of Python.\n")
fp.write ("See you soon!\n")
fp.close ()

fp = open (path, 'rt')
print (fp.read (), end='')
print ("================================================================")
fp.close ()

path = r"../data/sample_Append.txt"
fp = open (path, 'at')
fp.write ("This is an existing File.\n")
fp.write ("It is to test the write() method in Append mode of Python.\n")
fp.write ("See you soon!\n")
fp.close ()

fp = open (path, 'rt')
print (fp.read (), end='')
print ("================================================================")
fp.close ()

path = r"../data/sample_Write.txt"
fp = open (path, 'at')
fp.writelines (["Hello World! Opened an existing File.\n", "It is to test the writelines() method.\n", "Over and Out.\n"])
fp.close ()

fp = open (path, 'rt')
print (fp.read (), end='')
print ("================================================================")
fp.close ()

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# File Handling is an important feature for any program in the Real-World.
# Always specify a Path for the file in a separate variable for the ease of use in the program.
# In Windows, the Directory Path has '\' which is an Escape Sequence and cannot be used directly in the String.
# Therefore, the 'r' letter is used before the String containing the Directory Path to enforce it as a 'raw' String without escaping.

# The "open()" function can be used to open a file for operations.
# Syntax: open (filename, mode)
# There is a cursor which points to the beginning of the file when it is opened. It defines where the data has to be read or written in the file.
# There are 6 modes of opening a file:
# "r" - Read - Default value. Opens a file for Reading and generates an error if the file does not exist. The cursor position is at the begin.
# "r+" - Read and Write - Opens a file for Reading and Writing and generates an errot if the file does not exist. The cursor position is at the begin.
# "a" - Append - Opens a file for Appending and Creates the file if it does not exist. The cursor position is at the end. It doesn't overwrite the data.
# "a+" - Append and Read - Opens a file for Reading and Writing and Creates the file if it does not exist. The cursor position is at the end. It doesn't overwrite the data.
# "w" - Write - Opens a file for Writing and Creates the file if it does not exist. The cursor position is at the begin. It overwrites the data.
# "w+" - Write and Read - Opens a file for Reading and Writing. The cursor position is at the begin. It overwrites the data.
# "x" - Create - Creates the specified file and generates an error if the file exists.
# In addition to the above 6 modes, there is option to specify if the file shall be handled as Text - "t" (Default value)  or Binary mode - "b".
# The file should exist in the same directory path if only the name of the file is specified.
# Otherwise, the Absolute or Relative path of the file shall be provided.

# The "seek()" method can be used to change the cursor position of the file to a given specific position. It returns the new absolute cursor position.
# Syntax: seek (offset, reference_point)
# There are 3 reference points to which the cursor can be set:
# 0 - It sets the reference point at the beginning of the file. This is the default value.
# 1 - It sets the reference point at the current file position.
# 2 - It sets the reference point at the end of the file.
# The reference point at current file position or end of the file cannot be set in text mode except when offset is 0.
# The negative offset value can be provided to the method only if the file is opened in the Binary mode.
# After reaching the end of the file, it has to be reset before reading the file again. Otherwise, it will only be a blank.

# The "read()" method can be used to return a specific number of bytes from the file. The default value is -1 i.e. the whole file.
# Syntax: read (size)

# The "readline()" method can be used to return one line from the file. The number of bytes returned from the line can also be specified.
# The default is -1 i.e. the whole line. If the number of bytes exceed the length of the line, it does not return more than one line.
# Syntax: readline (size)

# The "readlines()" method can be used to return all the lines in a file as a List. The default is -1 i.e. all the lines will be returned.
# If the number of bytes returned exceed the hint number, no more lines will be returned.
# Syntax: readlines (hint)

# Note: ‘\n’ is treated as a special character of 2 bytes.

# The "close()" method can be used to close an opened file. It frees the memory space occupied by the file.
# It is used at the time when the file is no longer needed or if the file is to be opened in a different mode.
# It is necessary to close the file as in some cases, due to buffering, the changes made to a file may not show until the file is closed.
# Syntax: close ()

# The "write()" method can be used to write a specified text to the file. The mode in which the file is opened determines where the text will be written.
# Syntax: write (byte)

# The "writelines()" method can be used to write the items of a List to the file. The mode in which the file is opened determines where the text will be written.
# Syntax: writelines (list)
