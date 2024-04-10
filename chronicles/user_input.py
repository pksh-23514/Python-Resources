name = input ("What is your name?\nName: ")
print (f"Input Name: {name}")
age = input ("What is your age?\nAge: ")
print (f"Input Age: {age}")
print (type (name))
print (type (age))
age = int (age)
print (type (age))
print ("")

val = int( input ("Enter the Value: "))
print (val)
print (type (val))
print ("")

def read_Input ():
    while (True):
        user_input = input ("Enter the value (0-10): ")
        if (user_input.isdigit () == True):
            if (int (user_input) in range (0, 10)):
                return (int (user_input))
            else:
                print ("Incorrect Input Value. Please try again!")
        else:
            print ("Incorrect Input Data-Type. Please try again!")
val = read_Input ()
print (f"Input Value: {val}")

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# The User Input can be taked using the "input()" Built-in function. It takes the User Input and converts it into a String.
# Syntax: input (prompt)
# Where: 'prompt' is the default message to be displayed before asking for the User Input and is optional.
# When the "input()" function is called, it stops the program flow and waits for the User Input.
# After the User presses 'Enter key', the program flow resumes and the typed data is returned by the function in form of a String.
# The returned String can then be typecasted to the desired Data-Type.

# Since, there can be any input in form of a String from the User; Validation of the User Input is really important.
# The Data-Type as well as the Value shall be checked against certain criteria to ensure the User Input is correct.
