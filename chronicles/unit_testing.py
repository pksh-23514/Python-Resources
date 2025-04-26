# Code for validation using 'pylint' Library.
a = 1
b = 2
print (a)
print (B)
print ("")
# Comment the above code to run the below test code.

import sys
# Include the path for importing the Module to be validated.
sys.path.append ("../data")
# Import the Built-In 'unittest' Library.
import unittest
import unittest_file
# Define a Test Class inheriting "unittest.TestCase". Within the Test Class, define the individual Test Methods.
class TestCap (unittest.TestCase):
    # Test Method for the code.
    def test_one_word (self):
        text = "hello"
        result = unittest_file.cap_text (text)
        # Assertion to check the behavior of the code.
        self.assertEqual (result, "Hello")
    # Test Method for the code.
    def test_multiple_word (self):
        text = "hello world"
        result = unittest_file.cap_text (text)
        # Assertion to check the behavior of the code.
        self.assertEqual (result, "Hello World")
if (__name__ == "__main__"):
    unittest.main ()

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# Unit Testing is the first level of Software testing, where the smallest testable parts of the code are tested.
# This is used to validate that each software unit is performing as designed.
# There are several Third-party and In-Built testing tools available with Python (pylint, pyflakes, unittest, doctest etc.).

# pylint:
# -------
# 'pylint' is a library that helps in making the code to be more readable, understandable and simple errors present.
# Broadly, as a tool; it has the following features:
# 1. Lists out the errors which comes after execution of the code.
# 2. Enforces a Coding Standard and looks for the code smells.
# 3. Provides suggestions about the possible updates in certain code blocks.
# 4. Offers the details about the code’s complexity.
# This library needs to be installed (as it is a Third-party library) after Python is installed on the System using the below command:
# => pip install pylint
# To verify the 'pylint' installation, execute the below command:
# => pylint --version

# PEP 8, spelled PEP8 or PEP-8; is a document that provides guidelines and best-practices on how to write the Python code.
# To validate the code, run the below command:
# => pylint <file_name>
# The output of the command is a Score (out of 10.0) for the code and a Report about the possible issues in the code.
# If the Score is low, it doesn’t mean that the code is wrong. The Score represents how good/bad the code is understandable by another programmer.
# There are suggestions provided in the Report to improve the code. Each message consists of an ID and the suggestion/point.

# The ID starts with an alphabet followed by numbers. Each alphabet denotes the type of message object as described below:
# 1. Convention (C) - It is displayed when the program is not following the Standard rules.
# 2. Refactor (R)   - It is displayed for the bad code smell.
# 3. Warning (W)    - It is displayed for the Python specific problems.
# 4. Error (E)      - It is displayed when a particular line of code execution results in some error.
# 5. Fatal (F)      - It is displayed when 'pylint' has no access to further process a line of code.
# The common suggestions raised by 'pylint' are related to the styling issues (like comments, extra newline, modules and functions, variable names etc.).
# Any kind of 'pylint' identified error needs to be resolved before the code can be executed successfully.

# Note: The 'pylint' module will use the Uppercase naming convention by default. However, this behavior can be overridden.
# The regular expression used to identify the Uppercase convention is "(([A-Z_][A-Z1-9_]*)|(__.*__))$".
# To accept the identifiers with Lowercase alphabets, the regular expression should be added as a suggestion using the below command:
# => pylint --const-rgx='[a-z\_][a-z0-9\_]{2, 30}$' <file_name>

# unittest:
# ---------
# 'unittest' is a library that provides a set of tools for testing the code's functionality. This is a Built-in Library.
# It is more systematic and organized testing framework. It allows to create test cases, fixtures and suites to verify the code behavior.
# It allows to write test methods within Classes that check different aspects of the code (such as input, output and boundary cases).
# It also supports the test discovery that eases the process of automation of test execution across the project.

# The steps to write the test cases are as follows:
# 1. Import the 'unittest' library in the test code.
# 2. Define a Class that will inherit from the 'unittest.TestCase'. It shall contain all the test methods to validate the code.
# 3. Define the individual test methods in the Class. The method name must have the "test_" prefix to be discovered by the testing framework.
# 4. Write the Assertions inside each of the test method to compare the actual vs expected output for the function being tested.
# 5. Define the "unittest.main()" method for providing a command line interface to run the test.
# 6. Run the test file from the command line using the below command:
# => python3 -m unittest <file_name>
# Note: The "-v" option can be passed to the above command for obtaining a more detailed test results.
# => python3 -m unittest -v <file_name>

# The 'TestCase' Class provides seveal assert methods to check for and report the failures.
# 1.  assertEqual(first, second) => first == second
# 2.  assertNotEqual(first, second) => first != second
# 3.  assertTrue(expr) => bool(expr) is True
# 4.  assertFalse(expr) => bool(expr) is False
# 5.  assertIs(first, second) => first and second are identical objects
# 6.  assertIsNot(first, second) => first and second are not identical objects
# 7.  assertIsNone(expr) => expr is None
# 8.  assertIsNotNone(expr) => expr is not None
# 9.  assertIn(member, container) => member is present in the container
# 10. assertNotIn(member, container) => member is not present in the container
# 11. assertIsInstance(obj, class) => obj is an instance of the class
# 12. assertNotIsInstance(obj, class) => obj is not an instance of the class
# 13. assertRaises(exception, callable, *args, **kwds) => Tests if an exception is raised when callable is called with the passed arguments.

# There are 3 possible outcomes of the 'unittest' testing framework:
# 1. OK – This means that all the tests are passed.
# 2. FAIL – This means that the test did not pass and an "AssertionError" exception is raised.
# 3. ERROR – This means that the test raises an exception other than "AssertionError".
