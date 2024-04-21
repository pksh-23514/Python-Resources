import sys
sys.path.append ("../data")

# As soon as the Module is imported, the statements at the indentation level-0 for the Module is executed immediately.
import imported_module

# Module Function call
imported_module.display ()

if (__name__ == "__main__"):
    print (f"File {__name__} is being run directly!")
else:
    print (f"File {__name__} is being imported in the Program!")

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# Since there is no "main()" function in Python, when a Python program is executed by the interpreter; the code that is at 'level-0' indentation is to be executed.
# The "main()" function is implicitly all the code that is at 'level-0' indentation.
# The functions and classes that are written in the code are defined, but none of their code gets executed.
# However, before the execution, it defines a few Special Variables.
# '__name__' is a Built-in variable which evaluates to the Name of the current Module.
# While executing a Python Module, it is beneficial to know whether the Module is being run directly or the Module is imported in the program.
# If the Module is executed directly, the interpreter sets the '__name__' variable to have a value '__main__'.
# If the Module is imported in the program, the interpreter sets the '__name__' variable to the Module's name.
# Thus, an If-condition can be used to check whether the current file is being run on it's own or being imported somewhere else.
