count = 0
while (count < 5):
    print (f"Value: {count}")
    count = count + 1
print ("")

count = 0
while (count < 5):
    print (f"Value: {count}")
    count += 1
else:
    print ("count is greater than 5!")
print ("")

count = 0
while (count < 5):
    print (f"Value: {count}")
    count += 1
    if (count > 2):
        print ("The loop is broken!")
        break
else:
    print ("count is greater than 5!")
print ("")

i = 5
while (i > 0):
    j = 0
    while (j < i):
        print ("*", end='')
        j += 1
    print ("")
    i -= 1

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# The 'while' loop is used to execute a block of statements repeatedly until a given condition is satisfied.
# The 'while' loop Syntax is:
# ===========================
# while condition:
    # statements to be executed repeatedly
# statements outside of the while-loop as the indentation has been removed

# The Infinite 'while' loop can be performed if the condition is always True.
# This can be a common source of error if the condition is not fixed properly or if the iterator variable is not incremented / decremented inside the loop.

# Nested 'while' loops means 'while' loops under 'while' loops.
# The Nested 'while' loop Syntax is:
# ==================================
# while condition:
    # while condition:
        # statements to be executed inside the Inner loop
    # statements to be executed inside the Outer loop
# statements outside of the Nested loop as the indentation has been removed

# The 'else' statement in 'while' loop can be executed only after the condition becomes FALSE.
# If the loop is broken or if an Exception is raised, the Else statements will not be executed.
# The 'while-else' loop Syntax is:
# ================================
# while condition:
    # statements to be executed repeatedly
# else:
    # statements to be executed after the loop is terminated naturally
