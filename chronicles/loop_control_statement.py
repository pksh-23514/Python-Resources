my_str = "Hello World!"
for char in my_str:
    if (char == ' '):
        break
    print (f"{char}", end='')
print ("\n")

my_str = "LEVEL"
for char in my_str:
    if (char == 'E'):
        continue
    print (f"{char}", end='')
print ("\n")

for char in 'Python':
    pass
print ("Letter: ", char)

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# The Loop Control statements change the execution from their normal sequence.
# When execution leaves a scope, all automatic objects that were created in that scope are destroyed.
# There are 3 Loop Control statements: Break, Continue and Pass.

# The 'break' statement breaks out of the current closest enclosing loop.

# The 'continue' statement goes to the top of the current closest enclosing loop.

# The 'pass' statement does nothing at all.
# They are used to write empty Loops, Control statements, Functions and Classes.
# If the statement in the loop is left as empty or a comment is written, it will throw a Syntax error. So, 'pass' acts as a placeholder without creating the error.
