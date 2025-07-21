"""
Rules for Python variables:

    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)
    A variable name cannot be any of the Python keywords.

    Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John" 




Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John" 

"""
#You can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#The print() function is used to output variables
x = 13
print(x)

x = ("Python")
y = ("is")
z = ("awesome")
print(x, y, z)

#Create a variableoutside of a function, and use it inside the function
x = "awesome"
def myfunc():
    print("Python is " + x) 
myfunc()
#To create a global variable inside a function, you can use the global keyword
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)
#You can also use the global keyword to change a global variable inside a function
x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)
#create a variable with the same name as a global variable inside a function, and this will not change the global variable
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)