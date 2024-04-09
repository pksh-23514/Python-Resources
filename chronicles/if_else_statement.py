hungry = False
if (hungry == True):
    print ("Feed Me!")
print ("Not Hungry!")

count = 14
if (count > 23):
    print ("Greater!")
else:
    print ("Lesser!")

loc = "Bank"
pos = "Manager"
if (loc == "Bank"):
    if (pos == "Manager"):
        print (f"I am the {loc} {pos}!")

val = 75
if ((val > 75) and (val <= 100)):
    print ("Grade-A!")
elif ((val > 60) and (val <= 75)):
    print ("Grade-B!")
elif ((val > 40) and (val <= 60)):
    print ("Grade-C!")
else:
    print ("Fail!")

hungry = True
if (hungry == True): (print ("Feed Me!"))

count = 32
(print ("Greater!")) if (count > 23) else (print ("Lesser!"))

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# The If-Else statements are a part of the Conditional statements which decide the Control Flow of the code.
# It gives the code a choice to choose one of the 2 directions based on a particular condition.
# They accept Boolean values to decide the flow of the code.
# There are 4 types of If-Else statements:
# The 'if' statement
# The 'if-else' statement
# The 'nested-if' statement
# The 'if-elif-else' ladder

# The If-Else statements make use of ':' colon and '    ' indentation (whitespace) and it is very crucial part of the syntax.

# The If statement Syntax:
# ========================
# if condition:
   # Statements to execute if the condition is true.

# The If-Else statement Syntax:
# =============================
# if condition:
    # Statements to execute if the condition is true.
# else:
    # Statements to execute if the condition is false.

# The Nested-If statement Syntax:
# ===============================
# if (condition-1):
   # Statements to execute if the condition-1 is true.
   # if (condition-2):
      # Statements to execute if the condition-2 is true.
   # Block-2 ends here.
# Block-1 ends here.

# The If-Elif-Else statement Syntax:
# ==================================
# if (condition-1):
   # Statements to execute if the condition-1 is true.
# elif (condition-2):
   # Statements to execute if the condition-2 is true.
# ...
# All the series of conditions and their respective statements.
# ...
# else:
   # Statements to execute if all the conditions are false.

# Short hand If statement Syntax:
# ===============================
# if condition: Statements to execute if the condition is true.

# Short hand If-Else statement Syntax:
# ====================================
# (Statements to execute if the condition is true.) if condition else (Statements to execute if the condition is false.)
