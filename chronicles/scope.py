# **************************************************************
# Local Scope
def inner ():
    pi = 'local pi variable'
    # Local Scope resolution for the variable 'pi' is used.
    print (pi)
inner ()
print ("")
# **************************************************************

# **************************************************************
# Global and Local Scopes
pi = 'global pi variable'
def inner ():
    pi = 'local pi variable'
    # Higer priority is for the locally defined variable 'pi' than the globally defined variable 'pi'.
    print (pi)
inner ()
# No Local Scope resolution for the variable 'pi'. So, the Global Scope resolution for the variable 'pi' is used.
print (pi)
print ("")
# **************************************************************

# **************************************************************
# Global and Local Scopes
pi = 'global pi variable'
def inner (pi):
    # The variable 'pi' received as the function argument is printed. It has the same value as the Global variable however, the Scope is not Global.
    print (pi)
    # The variable 'pi' is defined locally to the function.
    pi = 'local pi variable'
    print (pi)
# The globally defined value for the variable 'pi' is passed as an argument to the "inner()" function.
inner (pi)
# The Global Scope resolution for the variable 'pi' is used.
print (pi)
print ("")
# **************************************************************

# **************************************************************
# Global Scope for accessing
def func ():
    # Since, there is no locally defined variable 'pi', it accesses the globally defined variable 'pi'.
    print (pi)
pi = 'global pi variable'
func ()
print (pi)
print ("")
# **************************************************************

# **************************************************************
# Global Scope for modifying
def func ():
    global pi
    # Global variable cannot be printed without the above declaration as there is another assignment of the variable with same name 'pi' in the function.
    # So, the variable 'pi' in the "print()" will be assumed to be a Local variable and searched in the Local Scope. If not found, it will throw an error.
    print (pi)
    # Since the variable 'pi' is declared with a 'global' keyword, it can be modified within the function.
    # Otherwise, it would be assumed to be a locally defined variable.
    pi = 'local pi variable'
    print (pi)
pi = 'global pi variable'
func ()
# Modified value of the variable 'pi' is printed.
print (pi)
print ("")
# **************************************************************

# **************************************************************
# Global Scope for modifying elements in the Mutable Objects
arr = [10, 20, 30]
def change ():
    for i in range (0, len (arr)):
        arr [i] += 10
print (f"Before executing change: {arr}")
change ()
print (f"After executing change:  {arr}")
print ("")
# **************************************************************

# **************************************************************
# Global Scope for assigning the Mutable Objects
arr = [10, 20, 30] 
def change (): 
    global arr
    arr = [20, 30, 40]
print (f"Before executing change: {arr}")
change ()
print (f"After executing change:  {arr}")
print ("")
# **************************************************************

# **************************************************************
# Global Scope in Nested functions
def add ():
    x = 15
    def change ():
        global x
        x = 20
    # The locally defined variable 'x' has the higher precedence over the globally defined variable 'x'.
    print (f"Before making change: {x}")
    change ()
    # The locally defined variable 'x' has the higher precedence over the globally defined variable 'x'.
    print (f"After making change:  {x}")
add ()
# The globally defined variable 'x' was modified in the function "change()" and the modified value is printed.
print (f"Final Value: {x}")
print ("")
# **************************************************************

# **************************************************************
# # Local, Global and Enclosed Scopes for accessing
pi = 'global pi variable'
def outer ():
    pi = 'outer pi variable'
    def inner ():
        # Since, there is no locally defined variable 'pi' in "inner()" function, it is searched in the "outer()" function.
        # Here, 'nolocal' declaration of variable 'pi' is note required as there is not other locally defined variable 'pi' in "inner()" function.
        print (pi)
    inner ()
    print (pi)
outer ()
print (pi)
print ("")
# **************************************************************

# **************************************************************
# Local, Global and Enclosed Scopes for modifying
pi = 'global pi variable'
def outer ():
    pi = 'outer pi variable'
    def inner ():
        # The 'nolocal' declaration of variable 'pi' is used to reference the locally defined variable 'pi' from the "outer()" function.
        nonlocal pi
        # The variable 'pi' is searched in the hierarchy of: Local --> Enclosed --> Global
        # Since, there is a 'nonlocal' declaration, it is searched in the "outer()" function.
        print (pi)
        # Due to the 'nolocal' declaration of variable 'pi', it is modified from the "outer()" function.
        # Otherwise, it would be assumed to be a locally defined variable.
        pi = 'inner pi variable'
        print (pi)
    inner ()
    # The locally defined variable 'pi' is modified in the "inner()" function.
    print (pi)
outer ()
print (pi)
print ("")
# **************************************************************

# **************************************************************
# Local, Global, Enclosed and Built-in Scopes
# The Built-in Scope is introduced by importing the built-in library.
from math import pi
# Removed the globally defined variable 'pi'
#pi = 'global pi variable'
def outer ():
    # Removed the locally defined variable 'pi'
    #pi = 'outer pi variable'
    def inner ():
        # Remove the reference to the enclosed function variable
        #nonlocal pi
        # Since, the variable 'pi' is not defined in either Local, Enclosed or Global Scopes, the Built-in Scope is looked up.
        # The variable 'pi' is imported from the "math" module.
        print (pi)
    inner ()
outer ()

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# The Scope of a variable is the location where the variable can be located and accessed.
# A Scope defines the hierarchical order in which the Namespaces have to be searched in order to obtain the mappings of Name-to-Object (variables).
# It defines the accessibility and the lifetime of a variable.

# A Namespace is a system that has a unique name for each and every Object (variable or a method).
# It is a container where Names are mapped to Objects.
# When Python interpreter runs solely with the built-in functions (without any User-defined modules), they are present in Built-in Namespace.
# When there are User-defined modules, methods, classes etc.; a Global Namespace gets created.
# Later the creation of local functions creates the Local Namespace.
# The Built-in Namespace encompasses the Global Namespace and the Global Namespace encompasses the Local Namespace.
# The lifetime of a Namespace depends upon the Scope of the Objects. If the Scope of an Object ends, the lifetime of the Namespace comes to an end.
# Hence, it is not possible to access the Inner Namespace’s Objects from an Outer Namespace.

# The LEGB rule is used to decide the order in which the Namespaces are to be searched for Scope resolution.
# The scopes are listed below in terms of hierarchy (highest to lowest / narrowest to broadest):
# Local (L) - Defined inside function (not declared global in that function) / class.
# Enclosed (E) - Defined inside enclosing functions (Nested functions).
# Global (G) - Defined at the uppermost level of a file or declared global in the function within the file.
# Built-in (B) - Reserved names in Python Built-in modules.

# Local variables are initialized within a function and are unique to that function. It cannot be accessed outside the function.
# Any variable which is created or modified anywhere inside of a function is Local, if it hasn’t been declared as a Global variable.

# Global variables are defined outside any function and are not specified to any function. It can be accessed in any part of the program.
# The keyword 'global' is used to create Global variables from a non-global scope i.e. inside a function.
# It is used in the function only when there is an assignment or modifying to the Global variable. It is not required for accessing or printing.
# If a variable is assigned a value anywhere within the function’s body, it’s assumed to be a Local unless explicitly declared as Global.
# There is no need to use Global keywords outside a function.
# Variables that are only referenced inside a function are implicitly Global.

# The keyword 'nonlocal' is used only in Nested functions. It is used to reference a variable in the nearest scope.
# It works in a similar way as 'global' but unlike 'global', this keyword declares a variable to point to the variable of an outside enclosing (nested) function.
# It won't work on Local or Global variables and therefore must be used to reference variables in another scope except the Global or Local one.
# Since the referenced variable is reused, the Memory address of the variable is also reused and therefore it saves Memory.

# Note: It is not preferred to modify the Global variable inside the function.
#       The better way is to return the modified value from the function and reassign the returned value to the Global variable outside the function.
#  Eg.- x = 23
#       def func (x):
#           x = 14
#           return x
#       x = func (x)

# The "globals()" Built-in function returns a Dictionary containing the current Global Symbol table i.e. all the variables defined in the Global Scope of the Program.
# The "locals()" Built-in function returns a Dictionary containing the current Local Symbol table i.e. all the variables defined the Local Scope of the function.
