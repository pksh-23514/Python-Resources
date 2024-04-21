import sys
sys.path.append ("../data")

import my_package.my_sub_package.my_module
my_package.my_sub_package.my_module.display ()
print (my_package.my_sub_package.my_module.my_list)
print ("")

from my_package import my_module
my_module.display ()
print (my_module.my_list)

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# A Python Package is a collection/folder of Python Modules that work together to provide certain functionality.
# Packages are a way to organize and structure your Python code into reusable components.
# They keep the code organized, make it easier to manage and maintain and allow code sharing.
# To create a Package, the following steps have to be followed:
# 1. Create a directory to serve as the root of your Package structure.
# 2. Within the directory, write various Python files (Modules) containing the code. Each Module shall represent a distinct functionality or component of the Package.
# 3. Include an '__init__.py' file in the directory. It can be empty or can contain initialization code for the Package.
# Note: The '__init__.py' file signals the interpreter to treat the directory as a Package.
# 4. Include the sub-Packages within the Package by adding additional directories containing Modules and their own '__init__.py' file.
# Note: Don't name the sub-Packages having a '-' minus character in the name as it generates a SyntaxError. Eg.- sub-package_1
# 5. To use the Modules of a Package, import them in your program using the '.' dot notation.
# 6. To distribute the package for others to use, create a 'setup.py' file using Python’s setuptools library.
# Note: The 'setup.py' file defines the metadata about the Package and specifies how it should be installed.

# Syntax: import <package_name>.<sub_package_name>.<module_name>
# Syntax: from <package_name>.<sub_package_name> import <module_name>
# Eg.- Consider the below Package structure:
# package/
# |
# |-- __init__.py
# |-- module_1
# |-- sub_package_1
#     |
#     |-- __init__.py
#     |-- module_1
# |-- sub_package_2
#     |
#     |-- __init__.py
#     |-- module_1
# 1. Importing 'module_1' from 'sub_package_1' and calling any function inside it can be written as:
# => import package.sub_package_1.module_1
# => package.sub_package_1.module_1.<function_name>
# 2. Importing 'module_1' from 'sub_package_2' and calling any function inside it can be written as:
# => from package.sub_package_2 import module_1
# => module_1.<function_name>

# The search method for importing a Package is same as the process used for the Modules.
# If a Package is to be imported from the directory not present in any of the above 3 Lists, there is one simple way to add the path to the List.
# Using the "append()" method, the desired directory path containing the Package can be added to the 'sys.path' List of directories.
