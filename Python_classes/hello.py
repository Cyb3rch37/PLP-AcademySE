print("Hello, World!") #This is a comment


#sample code to print python version
import sys
print(sys.version)

#identation in python indicate a block of code
if 5 > 2:
  print("Five is greater than two!") 

#the hash sign is used to create a comment in python

#Multi line commenting
"""Since Python will ignore string literals 
that are not assigned to a variable, 
you can add a multiline string (triple quotes) 
in your code, and place your comment inside it:"""


#Variables - they are containers for storing data values
x = 5
y = "John"

print(x)
print(y)

x = 5
x = "Sally"

print(x)

#Casting - to specify the data type of a variable
"""
x = str(3)#x will be '3'
y = int(3)#x will be 3
z = float(3)#x will be 3.0
"""

#Get the data type of a variable using type()
x = 5
y = "Sally"

print(type(x))
print(type(y))