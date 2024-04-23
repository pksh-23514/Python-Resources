try:
    print (x)
except NameError:
    print ("Undefined variable detected!")
print ("")

try:
    res = 1 / 3
except:
    print ("Division by Zero is not allowed!")
else:
    print (f"Result: {res}")
print ("")

try:
    fp = open ('sample.txt', 'r')
    fp.write ("Testing Write operation...")
except IOError as err:
    print (err)
else:
    print ("Write operation successful!")
    fp.close ()
print ("")

num = 5
try:
    if (num % 2 == 1):
        raise Exception ("Error: The Number shall be Even!")
    else:
        print ("The Number is Even!")
except Exception as err:
    print (err)
print ("")

a = 5
try:
    sum = a + 14
finally:
    print ("This code is always executed!")
print (f"Sum: {sum}")
print ("")

try:
    fp = open ('sample.txt', 'r')
    fp.write ("Testing Write operation...")
except IOError as err:
    print (err)
finally:
    print ("The execution is over!")
print ("")

def divide (x, y):
    try:
        res = x / y
    except ZeroDivisionError:
        print ("Please change the Denominator to a non-Zero value!")
    except:
        print ("Something went Wrong with the Operation!")
    else:
        print (f"Result: {res}")
    finally:
        print ("This is the Division Operation!")
divide (1, 0)
divide (1, 'g')
divide (14, 5)
print ("")

# Nested Exception Handling
def divide (x, y):
    try:
        val = 50
        x.append (val)
    except AttributeError as err:
        print (err)
    else:
        try:
            result = [i / y for i in x]
            print (result)
        except ZeroDivisionError:
            print ("Please change 'y' argument to non-zero value")
    finally:
        print ("This is the Division Operation!")
x = [40, 65, 70, 87]
divide (x, 3)
divide (4, 3)
divide (x, 0)
print ("")

"""
**************************************************************
**************************************************************
"""
# Input Validation
def ask_for_int ():
    while True:
        try:
            val = int (input ("Enter the Interger: "))
        except:
            print ("The value entered is not an Integer. Please try again!")
            continue
        else:
            print (f"The value entered is an Integer: {val}")
            break
        finally:
            print ("End of the function block!")
ask_for_int ()
print ("")

"""
**************************************************************
**************************************************************
"""
# File Handling
def file_editor (path, text, mode):
    try:
        fp = open (path, mode)
        try:
            fp.write (text)
        except:
            print ("Unable to Write the Data!\n=> Please add an append (a) or write (w) Mode to the open() function.")
        else:
            print ("Write Operation successful!")
        finally:
            fp.close ()
    except:
        print (f"{path} file is not found!")
text = "Hello World!"
path = 'file_editor.txt'
mode = 'r'
file_editor (path, text, mode)
path = '../data/file_editor.txt'
mode = 'r'
file_editor (path, text, mode)
mode = 'w'
file_editor (path, text, mode)

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# Errors are the (syntactical) problems in a program due to which the program will stop the execution.
# Exceptions are raised when some internal (logical) events occur which changes the normal flow of the program.
# Both Errors and Exceptions are a type of Run-time Error, which means they occur during the execution of a program.

# When an Error or Exception is raised, it is handled with the help of Handling method.
# Errors and Exceptions Handling allow the execution of the program to continue even if there is some problems encountered.
# There are 3 keywords for Handling any potential errors: try, except and finally.
# The 'try' block is used to test a block of code for errors.
# The 'except' block is used to handle the error generated.
# The 'finally' block is used to execute the code, regardless of the result of the 'try' and 'except' blocks.

# The 'try-except-else' block can handle a single or multiple Errors/Exceptions.
# Syntax:
# try:
#     Statements to be tested for errors.
#     ...
# except Exception_1:
#     Statements to execute if the corresponding error is encountered.
#     ...
# except Exception_2:
#     Statements to execute if the corresponding error is encountered.
#     ...
# ...
# else:
#     Statements to execute if no errors are encountered.
# Note: The 'except' block can be used to check any Exception using "except:" syntax without providing the specific type of 'Exception' to be checked.
# Note: The specific 'Exception' can be checked and the stored message can be displayed. The 'as' keyword stores the message in a variable.

# The 'try-except' block can be used with the 'raise' keyword for matching the error generated with the kind of errors in 'except' block.

# The 'finally' block can be placed after the 'try-except-else' blocks.
# Syntax:
# try:
#     Statements to be tested for errors.
#     ...
# except Exception:
#     Statements to execute if the corresponding error is encountered.
#     ...
# finally:
#     This code block is always executed.
#     ...
# Note: The 'finally' block is quite useful in cleaning up the resources and closing the Objects (especially in File-handling).

# Nested Exception Handling in Python is used to handle multiple Errors/Exceptions in a sequence.
# They are very helpful in scenarios where all the steps of the code have a chance for error generation.
# Syntax:
# try:
#     Statements to be tested for errors.
#     ...
# except Exception_1:
#     Statements to execute if the corresponding error is encountered.
# else:
#     try:
#         Statements to be tested for errors.
#         ...
#     except:
#         Statements to execute if the corresponding error is encountered.
#         ...
# finally:
#     This code block is always executed.
