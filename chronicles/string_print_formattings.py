val = 'INSERTED'
print ('This is a String {}.'.format (val))

print ('{} {} {}'.format ('World', '!', 'Hello'))
print ('{2} {0} {1}'.format ('World', '!', 'Hello'))
print ('{str3} {str1} {str2}'.format (str1='World', str2='!', str3='Hello'))

res = 100/7
print ("RESULT: {r}".format (r=res))
print ("RESULT: {r:1.3f}".format (r=res))
print ("RESULT: {r:10.3f}".format (r=res))

val = 'INSERTED'
print (f'This is a String {val}.')

str1 = "Hello"
str2 = "World"
str3 = "!"
print (f"{str1} {str2} {str3}")

newline = '\n'
print (f"newline: {newline}")

"""
**************************************************************
**************************************************************
"""
# Summary:
# ========
# String Interpolation is the method to inject a variable into the String for printing.
# There are multiple ways to format Strings for printing variables in them:
# The "format()" method formats the specified values and insert them inside the String's placeholders '{}'.

# The placeholders can be indexed based on the values ordering in the String. The index starts from '0' to 'n-1'.

# The placeholders can be assigned names based on the values ordering in the String.

# The placeholders can be included with the a lot of formatting types.
# :< - Left aligns the result (within the available space)
# :> - Right aligns the result (within the available space)
# :^ - Center aligns the result (within the available space)
# := - Places the sign to the left most position
# :+ - Use a plus sign to indicate if the result is positive or negative
# :- - Use a minus sign for negative values only
# : - Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
# :, - Use a comma as a thousand separator
# :_ - Use a underscore as a thousand separator
# :b - Binary format
# :c - Converts the value into the corresponding unicode character
# :d - Decimal format
# :e - Scientific format, with a lower case e
# :E - Scientific format, with an upper case E
# :f - Fix point number format
# :F - Fix point number format, in uppercase format (show inf and nan as INF and NAN)
# :g - General format
# :G - General format (using a upper case E for scientific notations)
# :o - Octal format
# :x - Hex format, lower case
# :X - Hex format, upper case
# :n - Number format
# :% - Percentage format

# The Float formatting allows to set the Precision and Width for the Decimal value.
# Syntax for Float formatting: "{<value>:<width>.<precision>f}"
# Where: 'value' is the value. 'width' is the total number of positions in which the value shall be written. 'precision' is the number of Decimal points.

# The "f-strings" is a relatively new feature added in Python 3.6 version. This formatting mechanism is known as Literal String Interpolation.
# To create an f-string, prefix the String with the letter "f".
# However, the Backslash cannot be used in the format String directly as it is a syntax error as per the documentation.
# It throws an error: SyntaxError: f-string expression part cannot include a backslash
# The workaround is to put the backslash into a variable.

# To suppress a newline, 
# https://ioflood.com/blog/python-print-without-newline/
