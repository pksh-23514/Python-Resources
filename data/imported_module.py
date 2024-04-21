def display ():
    print ("Hello, I am in the Module file!")

print ("Welcome to the Python Modules!")

if (__name__ == "__main__"):
    print (f"File {__name__} is being run directly!")
else:
    print (f"File {__name__} is being imported in the Program!")
