# Concepts to cover today: variables, loops, conditionals, functions and lists
# Variables

msg = "Hello, Python!";

# How to comment in python is using #

print (msg);

if 5 > 2 :
  print ("Five is greater than two!");

if 2 < 5:
  print ("Two is less than 5, I guessed it. Then its correct");

# Variables in use

x = 5
y = "Hello, world"

print(x,y)

"""
This is the comment
block that is taking more than one space
"""

"""
This is my second comment block
Find it here please.
"""


"""
  W3Schools Python Lecture on variables
"""

x = 5
y = "john"

print(x)
print(y)

# changing the datatype of a given variable

print ("********************** New challenge here *****************************")
x = x * 2
z = x
print(x)
print(z)

print ("********************** Python Casting *****************************")

a = str("My name is kevin")
b = int(20)
c = float(20.0001)

print(a, " and I am ", b, "this is a unit conversion", c)


# Assigning multiple values to different variables inline way

x, y, z = 5, 6, 7

print(x,y,z)

d = e = f = "Oranges are sweet"

print(d,e,f)
print ("Hello", "World")

# Global variables

global_val = "I am a global value"

def myFunc():
  print("This is", global_val)

myFunc()


# Using a global variable inside a function block, using the "global" keyword

def functCall():
  global global_inside_val
  global_inside_val = "I am using global keyword"
  print (global_inside_val, "The variable is of type", type(global_inside_val))

functCall()

# Type casting of Numbers

cast_number_1 = 5
cast_number_2 = 12.0
cast_number_3 = -2j

print(float(cast_number_1))
print(int(cast_number_2))
print(complex(cast_number_2))
