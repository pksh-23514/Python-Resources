print ((lambda x : x * 2) (3))

upper = lambda my_str : my_str.upper ()
print (upper ("hello"))
print (upper ('world'))
print ("")

x = lambda a, b, c : a + b + c
print (x (5, 6, 2))
print ("")

largest = lambda x, y : x if (x > y) else y
print (largest (5, 23))
print ("")

format_numeric = lambda num: (f"{num:e}") if isinstance (num, int) else (f"{num:,.2f}")
print ("Int formatting:", format_numeric(1000000))
print ("Float formatting:", format_numeric(999999.789541235))
print ("")

sqr = [lambda arg = x: (arg * arg) for x in range (5)]
print (sqr)
for num in sqr:
    print (num (), end=' ')
print ("")
print ([(lambda x: (x * x)) (x) for x in range (5)])
print ("")

def my_func (num):
    return (lambda mul : mul * num)
my_doubler = my_func (2)
my_tripler = my_func (3)
print (my_doubler (14))
print (my_tripler (14))
print ("")

my_list = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
double_list = map ((lambda x: (x * 2)), my_list)
for num in double_list:
    print (num)
print ("")

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map ((lambda x, y: x + y), numbers1, numbers2)
print (result)
print(list(result))
print ("")

my_list = ['sat', 'bat', 'cat', 'mat']
result = list (map (list, my_list))
print(result)
print ("")

my_list = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
odd_list = list (filter ((lambda x: (x % 2 != 0)), my_list))
even_list = list (filter ((lambda x: (x % 2 == 0)), my_list))
print (odd_list)
print (even_list)
print ("")

ages = [13, 90, 17, 59, 21, 60, 5]
adults = filter ((lambda x: (x > 18)), ages)
print (adults)
print (list (adults))
print ("")

def vowels (char):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (char in letters):
        return True
    else:
        return False
my_list = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
result = filter (vowels, my_list)
for char in result:
    print (char)

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# Lambda functions are small anonymous functions i.e. the function is without a name.
# It can have any number of arguments but only one expression, which is evaluated and returned.
# There is no 'return' statement because the anonymous function will automatically return the result of the expression in the function.
# They are throw-away functions i.e. they are used only once and never referenced. However, they can be called multiple times if assigned to a variable name.
# They can be used whenever function objects are required.

# Syntax:
# lambda arguments : expression
# There can be any number of arguments.
# They are syntactically restricted to a single expression.

# The Short hand form of If-Else can be very handy to implement a conditional check using the Lambda function.

# With List Comprehensions, the Lambda functions can be used in two ways.
# The first way is to create a List of different Lambda functions using List Comprehensions and iterate through the List to evaluate the final value for each.
# The second way is to call the Lambda function multiple times and return the final values in form of a List using the List Comprehensions.

# The power of Lambda functions can be better shown when they are used inside another function.
# Eg. - The same function definition can be used to perform the multiplication with the value 2 or 3 with the help of Lambda function.

# The first use case is with the "map()" function.
# Syntax: map (func, iter)
# Where: 'func' is a function name which "map" passes to each element in the iterable. 'iter' is the one or more iterable which is mapped.
# It returns the Map Object containing the list of results after applying the given function to each item of the given iterable.
# The returned Map Object can be passed to "list()" or "set()" for displaying the results in the specified format.

# The second use case is with the "filter()" function.
# Syntax: filter (func, iter)
# Where: 'func' is a function name that tests each element in the iterable for True or False. 'iter' is the iterable (only one at a time) that needs to be filtered.
# It returns the Filter Object containing the list of results that is filtered based on the passed function.
# The returned Filter Object can be passed to "list()" or "set()" for displaying the results in the specified format.
