# Built-in Modules
import math
print (math.sqrt (9))
print (math.factorial (4))
print ("")

from math import sqrt, factorial
print (sqrt (16))
print (factorial (5))
print ("")

from math import *
print (sqrt (25))
print (factorial (6))
print ("")

# User-defined Modules
import sys
print (sys.path)
print ("")

sys.path.append ("../data")
print (sys.path)
print ("")
import my_module
my_module.welcome ()
print ("")

from my_module import display
display ()
print ("")

import my_module as mod
print (mod.my_list)
print (dir (mod))

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# A Python Module is a file containing Python definitions and statements.
# Modules can define functions, classes and variables. It can also include runnable code.
# Grouping related code into a Module makes the code easier to understand and use. It also makes the code logically organized.
# To create a Module, write the desired code and save that in a file with any suitable file name and '.py' extension.
# To import the functions and classes defined in a Module, the 'import' statement is used.
# When the interpreter encounters an import statement, it imports the Module if the Module is present in the Search Path.
# A Search Path is a list of Directories that the interpreter searches for importing a Module.
# Syntax: import <module>
# Where: 'module' is the Python file name written without the '.py' extension.
# This does not import the functions, classes or variables directly instead imports the Module only.

# To access the functions inside the Module, the '.' dot operator is used.
# Syntax: <module_name>.<function_name>

# To access the variables inside the Module, the '.' dot operator is used. They can be variables of any Data-Type.
# Syntax: <module_name>.<variable_name>

# To import certain specific attributes from a Module without importing the Module as a whole, the 'from' statement is used.
# Syntax: from <module_name> import <attribute_name-1, attribute_name-2, ...>
# Where: 'attribute_name' can be the name of the function, class or variable. Multiple attributes can be imported at once.
# When importing using the 'from' keyword, the Module name is not used for accessing the specific attribute (as shown earlier using the dot-operator).
# The attribute can be accessed directly using it's name as if it has been defined in the current scope.

# If the attributes that will be required in the program is not exactly known, it is recommended to import all the names from the Module.
# The '*' symbol used with the 'import' statement is used to import all the names from a Module to a current namespace.
# Syntax: from <module_name> import *

# Whenever a Module is imported, the Interpreter looks for several locations orderly to find the Module as defined below:
# First, the Module is searched in the current directory.
# If the Module isn’t found in the current directory, then each directory in the shell variable 'PYTHONPATH' is searched for the Module.
# Note: The PYTHONPATH is an environment variable, consisting of a list of directories.
# If that also fails, finally the Module is searched in the installation-dependent list of directories configured at the time Python is installed.
# The Directory List where the Module is searched is stored in the 'sys.path' Built-in variable.

# If a Module is to be imported from the directory not present in any of the above 3 Lists, there is one simple way to add the path to the List.
# Using the "append()" method, the desired directory path containing the Module can be added to the 'sys.path' List of directories.
# The 'sys.path.append()' is the most basic and commonly used method to import Modules from different directories.
# However, it has a potential pitfall, it only affects the current session i.e. if Python is closed and re-opened, 'sys.path' will be reset to default values.

# The Modules can be renamed to create an alias using the 'as' keyword.
# Syntax: import <module_name> as <alias_name>

# To list all the properties and methods in a Module, the "dir()" function can be used.
# This function returns a List of all the properties and methods, even built-in properties which are default for all the objects.
