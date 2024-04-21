class Person:
    # Class attribute
    attr = "Mammal"
    # Instance attribute
    def __init__ (self, name):
        self.name = name
    def say_hi (self):
        print (f"Hello, my name is {self.name}")
obj1 = Person ("Rodger")
obj2 = Person ("Tommy")
# Accessing Classes attribute
print (f"Rodger is a {obj1.__class__.attr}")
print (f"Tommy is a {obj2.__class__.attr}")
# Accessing Instance attribute
obj1.say_hi ()
obj2.say_hi ()
print (type (Person))
print (type (obj1))
print (type (obj2))
print ("")

class Circle:
    pi = 3.142
    def __init__ (self, radius=1):
        self.radius = radius
        self.area = Circle.pi * (self.radius ** 2)
    def getCircumference (self):
        return (2 * self.pi * self.radius)
c1 = Circle ()
c2 = Circle (7)
print(f'Radius is: {c1.radius}')
print(f'Area is: {c1.area}')
print(f'Circumference is: {c1.getCircumference()}')
print(f'Radius is: {c2.radius}')
print(f'Area is: {c2.area}')
print(f'Circumference is: {c2.getCircumference()}')
print ("")

# Base Class
class Animal:
    def __init__ (self):
        print ("Animal created!")
    def who_am_I (self):
        print ("I am a Mammal.")
    def eat (self):
        print ("I am eating...")
# Derived Class
class Dog (Animal):
    def __init__ (self):
        Animal.__init__ (self)
        print ("Dog created!")
    def bark (self):
        print ("Woof!")
my_dog = Dog ()
my_dog.who_am_I ()
my_dog.eat ()
my_dog.bark ()
print ("")

class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def display (self):
        print (self.name, self.age)
class Student (Person):
    def __init__ (self, name, age, dob):
        self.stName = name
        self.stAge = age
        self.stDob = dob
        # Inheriting the properties of the Base Class using "super()" function
        super ().__init__ ("Rahul", age)
    def displayStudent (self):
        print (self.stName, self.stAge, self.stDob)
obj = Student ("Mayank", 23, "16-03-2000")
obj.display ()
obj.displayStudent ()
print ("")

# Multiple Inheritance
class Parent1:
    def __init__ (self):
        self.str1 = "Hi"
        print ("Father")
class Parent2:
    def __init__ (self):
        self.str2 = "Hello"
        print ("Mother")
class Child (Parent1, Parent2):
    def __init__ (self):
        Parent1.__init__ (self)
        Parent2.__init__ (self)
        print ("Child inherited from Father and Mother")
    def print_Str (self):
        print (self.str1, self.str2)
obj = Child ()
obj.print_Str ()
print ("")

# Multi-Level Inheritance
class Parent:
    def __init__ (self, name):
        self.name = name
    def getName (self):
        print (self.name)
class Child (Parent):
    def __init__ (self, name, age):
        Parent.__init__ (self, name)
        self.age = age
    def getAge (self):
        print (self.age)
class Grandchild (Child):
    def __init__ (self, name, age, address):
        Child.__init__ (self, name, age)
        self.address = address
    def getAddress (self):
        print (self.address)
obj = Grandchild ("Rahul", 23, "Mumbai")
obj.getName ()
obj.getAge ()
obj.getAddress ()
print ("")

class India:
    def capital (self):
        print ("New Delhi")
    def language (self):
        print ("Hindi")
class America:
    def capital (self):
        print ("Washington D.C.")
    def language (self):
        print ("English")
obj1 = India ()
obj2 = America ()
for country in (obj1, obj2):
    country.capital ()
    country.language ()
print ("")

class Bird:
    def intro (self):
        print ("There are a variety of species of Birds!")
    def flight (self):
        print ("Most of the birds can fly but some cannot.")
class Sparrow (Bird):
    def flight (self):
        print ("Sparrows can fly.")
class Ostrich (Bird):
    def flight (self):
        print ("Ostriches cannot fly.")
obj_bird = Bird ()
obj_spr = Sparrow ()
obj_ost = Ostrich ()
obj_bird.intro ()
obj_bird.flight ()
obj_spr.intro ()
obj_spr.flight ()
obj_ost.intro ()
obj_ost.flight ()
print ("")

# Abstract Class
class Animal:
    def speak (self):
        raise NotImplementedError ("Sub-Class must be implemented for this method")
    def name (self):
        raise NotImplementedError ("Sub-Class must be implemented for this method")
class Dog (Animal):
    def speak (self):
        print ("Woof!")
    def name (self):
        print ("Nikko")
class Cat (Animal):
    def speak (self):
        print ("Meow!")
    def name (self):
        print ("Felix")
animals = [Dog (), Cat ()]
for animal in animals:
    animal.speak ()
obj1 = Dog ()
obj2 = Cat ()
def func (obj):
    obj.name ()
func (obj1)
func (obj2)
print ("")

# Protected Member
class Base:
    def __init__ (self):
        self._a = 23
class Derived (Base):
    def __init__ (self):
        Base.__init__ (self)
        print ("Calling the Protected member inside of Derived Class: ", self._a)
        # Modifying the Protected member
        self._a = 5
        print ("Calling the modified Protected member of Base Class: ", self._a)
obj1 = Derived ()
obj2 = Base ()
# Protected member can be accessed outside of the Base Class but should not be done due to convention
print ("Accessing the Protected member of obj1: ", obj1._a)
print ("Accessing the Protected member of obj2: ", obj2._a)
print ("")

# Private Member
class Base:
    def __init__ (self):
        self.a = 14
        self.__b = 23
        print ("Calling the Private member inside of Base Class: ", self.__b)
    # The method of the Class can access and modify the Private variable
    def update (self):
        self.__b = 5
        print ("Calling the modified Private member of Base Class: ", self.__b)
obj = Base ()
print ("Accessing the Public member of obj1: ", obj1._a)
obj.update ()
print ("")

# Python’s Private members can be accessed outside the Class through Python Name Mangling.
class Base:
    def __init__ (self):
        self.__hidden = 23
obj = Base ()
# Accessing the Private members through Name Mangling
print ("Accessing the Private member of obj: ", obj._Base__hidden)
print ("")

class Sample:
    def __init__ (self):
        self.a = 23
        print ("Object Created!")
obj = Sample ()
print (obj)
print (obj.a)
print ("Object Deleted!")
del obj
# Uncommenting the below line will throw an error as: "NameError: name 'obj' is not defined"
# print (obj)

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# Object Oriented Programming (OOP) allows Users to create their own Objects and Classes. For larger Programs, OOP is required for organization and reusability.
# The main concept of OOPs is to bind the Data and the Functions that work on those Data as a single unit, so that no other part of the code can access this Data.

# Class is a collection of Objects. It is like an Object constructor that contains the blueprint or prototype from which the Objects are created.
# It is a logical entity that contains some attributes (characteristics) and methods (operations performed).
# Classes are created by keyword 'class'.
# Syntax: class <ClassName>:
#             def __init__(self, param1, param2, ...):
#                 self.param1 = param1
#                 self.param2 = param2
#                 ...
#
#             def <method_name>(self, param1, param2, ...):
#                 ...
#                 Operations to be performed
#                 ...
# The attributes and methods of a Class are accessed using the '.' dot operator.
# The attributes can be of 2 types: Class attributes and Instance attributes.
# Class attributes are shared by all instances of the Class. They can be accessed using the format: (Class_name or Object_name).attribute
# Instance attributes are specific to that instance of the Class. They can be accessed using the format: (Object_name).attribute
# Methods are functions defined inside the body of a Class. They can include Object parameters and other non-Object parameters passed.

# The "__init__" method is the default constructor used to initialize the Objects of the Class.
# The task of constructors is to initialize the Data Members of the Class when an Object of the Class is created.
# It contains a collection of statements that are executed automatically at the time of Object creation.

# The 'self' parameter is used to represent the current instance of the Class being used. It is always pointing to the current Object.
# Whenever, a method of an Object created from a Class is called, the Object is automatically passed as the first argument using the 'self' parameter.
# It is customary to use 'self' as the first parameter in methods of a Class. If it is not provided, an error is generated.
# It is a convention and not a keyword. Any other parameter name instead of 'self' can be used but 'self' is preferred name to increase the readability.

# Note: Since, Python is Dynamically-typed and flexible; proper documentation needs to be provided for the Object parameters to be passed.

# Object is an entity that has a State, Behavior and Identity assosciated with it. In Python, everything (integer, String, List etc.) is an Object.
# State is represented by the attributes of an Object. It also reflects the properties of an Object.
# Behavior is represented by the methods of an Object. It also reflects the response of an Object to other Objects.
# Identity gives a unique name to an Object and enables one Object to interact with other Objects.

# Inheritance is the capability of one Class to derive or inherit properties from another Class.
# The Class that derives it's properties is called Derived Class or Child Class.
# The Class from which the properties are being derived is called the Base Class or Parent Class.
# Syntax: class <Base_Class>:
#             Body
#         class <Derived_Class> (Base_Class):
#             Body
# It provides the reusability of a code. Also, it allows us to add more features to a Class without modifying it.
# It is transitive in nature, which means that if Class B inherits from Class A, then all the sub-Classes of B would automatically inherit from Class A.
# The methods of the Base Class are accessible to the Derived Class. The other methods defined in the Derived Class are only native to it.
# If the "__init__()" of the Base Class is not called, the instance variables defined there will not be available to the Derived Class.

# The "super()" is a Built-in function used to refer to the Base Class. It returns a proxy Object that represents the Base Class.
# It allows to access the Base Class's attributes and methods in the Derived Class. It enables method Overriding and Inheritance.
# The main benefit is there is no need to specify the Base Class name to access it's methods.

# There are 5 types of Inheritance:
# Single Inheritance - When a Child Class inherits from only one Parent Class, it is called Single Inheritance.
# Multiple Inheritance - When a Child Class inherits from multiple Parent Classes, it is called Multiple Inheritances.
# Multi-Level Inheritance - When a Child Class inherits from a Parent Class which in turn is inheriting from it's Parent Class, it is called Multi-Level Inheritance.
# Hierarchical Inheritance - When more than one Child Classes are inheriting from a single Parent Class, it is called Hierarchical Inheritance.
# Hybrid Inheritance - When it is a blend of more than one type of Inheritance, it is called Hybrid Inheritance.

# Polymorphism means the same function name (but different function signatures) being used for different types.
# The key difference is the Data-types of arguments and number of arguments used in the function.
# It lets us define the methods in the Child Class that have the same name as the methods in the Parent Class.
# The Child Class inherits the methods from the Parent Class that can be modified if the method inherited doesn't fit with the Child Class.
# This process of re-implementing a method in the Child Class is called Method Overriding.

# Abstract Class is a blueprint for other sub-Classes. It is a Class that contains one or more Abstract methods.
# An Abstract method is a method that has a declaration but does not have an implementation.
# By defining an Abstract Base Class, a common Application Program Interface (API) for a set of sub-Classes can be defined.
# Abstract Class is never instantiated i.e. no Object shall be created for this Abstract Class.
# An error statement is raised if an Object is raised for such Abstract Class.

# Encapsulation is the idea of wrapping data and methods that work on data within one unit.
# This puts restriction on accessing variables and methods directly and can prevent the accidental modifications of data.
# A Class is an example of Encapsulation as it encapsulates all the data i.e. member functions, variables, etc.
# The goal of Information Hiding is to ensure that an Object’s state is always valid by controlling access to attributes that are hidden from the outside world.
# Protected Members are by definition those members of the Class that cannot be accessed outside the Class but can be accessed from within the Class and its sub-Classes.
# To accomplish this in Python, the convention followed is by prefixing the name of the member by a single '_' underscore.
# Although the protected variable can be accessed out of the Class as well as in the Derived Class (modified too in derived class), it should be avoided.
# It is customary (convention not a rule) to not access the Protected members out the Class body.
# Private Members are by definition those members of the Class that can neither be accessed outside the Class nor by any of its sub-Classes.
# To prevent accidental changes, a Class’s Private variable can only be changed by the Class’s method and accessed inside the Class only.
# To accomplish this in Python, the convention followed is by prefixing the name of the member by a double '__' underscore.
# Nothing in Python is truly private; internally, the names of Private members are mangled and unmangled on the fly to make them seem inaccessible by their given names.

# Deleting an Object of the Class is done using the 'del' keyword.
# Since everything in Python represents an object in one way or another, it can be used to delete List, Dictionary, variables etc.
# Syntax: del object_name
