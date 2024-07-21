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
    # statements to be executed repeatedly.
# statements outside of the while-loop as the indentation has been removed.

# The 'else' statement in 'while' loop can be executed only after the condition becomes FALSE.
# If the loop is broken or if an Exception is raised, the Else statements will not be executed.
# The 'while-else' loop Syntax is:
# ================================
# while condition:
    # statements to be executed repeatedly.
# else:
    # statements to be executed after the loop is terminated naturally.
