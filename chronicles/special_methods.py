my_list = [1, 2, 3]
print (list)
class Sample:
    pass
print (Sample ())
print ("")

class Book:
    def __init__ (self, title, author, pages):
        print("A Book is created!")
        self.title = title
        self.author = author
        self.pages = pages
    def __str__ (self):
        return (f"{self.title} by {self.author}")
    def __len__ (self):
        return self.pages
    def __del__ (self):
        print ("A Book is destroyed!")
book = Book ("Python", "Robert", 514)
# Special Methods
print (book)
print (str (book))
print (len (book))
del (book)

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# Special methods are reserved by Python which affect the Objects's high-level behavior and it's interaction with Operators.
# They are also called as Magic method or Dunder method (as they use '__' double underscore).
# The "__init__()" method controls the process of creating the instances of a Class.
# The "__str__()" method returns String representation of the instances of a Class.

# The "x + y" invokes "x.__add__(y)".
# The "x - y" invokes "x.__sub__(y)".
# The "x * y" invokes "x.__mul__(y)".
# The "x / y" invokes "x.__truediv__(y)".
# The "x ** y" invokes "x.__pow__(y)".
# The "len(x)" invokes "x.__len__()".
# The "x[key]" invokes "x.__getitem__(key)".
# The "x[key] = item" invokes "x.__setitem__(key, item)".
# The "item in x" invokes "x.__contains__(item)".
# The "iter(x)" invokes "x.__iter__()".
# The "next(x)" invokes "x.__next__()".
