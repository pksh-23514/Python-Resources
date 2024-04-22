"""
num = -3
if (num < 0):
    raise Exception ("The Number shall be Positive!")
else:
    print ("The Number is Positive!")
O/P:
====
Traceback (most recent call last):
  File "raise_keyword.py", line 3, in <module>
    raise Exception ("The Number shall be Positive!")
Exception: The Number shall be Positive!
"""

num = -3
try:
    if (num < 0):
        raise Exception ("The Number shall be Positive!")
    else:
        print ("The Number is Positive!")
except Exception as err:
    print (err)
print ("")

num = 5
try:
    if (num % 2 == 1):
        raise ValueError ("The Number shall be Odd!")
    else:
        print ("The Number is Even!")
except ValueError as err:
    print (err)
print ("")

amount = 1999
try:
    if (amount < 2999):
        raise ValueError
    else:
        print ("Sufficient Balance!")
except ValueError:
    print ("ValueError: Please add money in your Account!")
print ("")

"""
try:
    res = 1 / 0
except ZeroDivisionError:
    raise ZeroDivisionError ("Cannot Divide by Zero!")
print ("")
O/P:
====
Traceback (most recent call last):
  File "raise_keyword.py", line 45, in <module>
    res = 1 / 0
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "raise_keyword.py", line 47, in <module>
    raise ZeroDivisionError ("Cannot Divide by Zero!")
ZeroDivisionError: Cannot Divide by Zero!
"""

s = "apple"
try:
    num = int (s)
except:
    raise

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# If there is a limitation or condition, the 'raise' keyword can be used to raise Error or Exception.
# Syntax: raise <Exception_name> ("Message to be displayed")
# Note: Both the 'Exception_name' and 'Message to be displayed' are optional and defined as per the need.
# Output:
# <Traceback Call>
# ...
# Exception_name: Message to be displayed

# The kind of Error/Exception to be raised and the message to be displayed can be defined.
# It is used to bring the current Error/Exception in a Handler so that it can be handled further up the call stack.
# It stops the execution of the further program. Hence, it has to be placed in a 'try-except' block for the further execution to continue.

# The Error/Exception is displayed along with a 'Traceback' call to the line which generated it.
# The message to be displayed can also be limited to just the message without the 'Traceback' call by using the 'try-except' block for the error.
# The message for the particular error can be matched with an 'except' block and stored in a variable to be printed.
# However, it also removes the 'Exception_name' from the output displayed.
# So, the better way is to just raise the type of error without any message and match the error in 'except' block with meaningful message to be displayed.

# When 'raise' keyword is used, there is no compulsion to give the 'Exception_name' along with it.
# If there is no 'Exception_name' with the 'raise' keyword, it re-raises the last occured Error/Exception.

# The 'raise' allows us to throw one Error/Exception at any time.
# It is very useful in case of Input Data Validation.
