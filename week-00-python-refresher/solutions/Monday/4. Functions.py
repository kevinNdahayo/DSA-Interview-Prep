# Functions in Python

def fahrenheit_to_celsius(temp):
  return (int(temp) - 32) * (5/9)


print(fahrenheit_to_celsius(37), "is the celsius degrees")
print(fahrenheit_to_celsius(77), "is the celsius degrees")
print(fahrenheit_to_celsius(95), "is the celsius degrees")
print(fahrenheit_to_celsius(50), "is the celsius degrees")

# 1. Positional Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Dog", "bear")
my_function(animal="Dog", name="Kovu")

def sort_fruits(fruits):
  for fruit in fruits:
    print(fruit)

sort_fruits(["Apple", "Banana", "Jack Fruit"])


def args_function(*kids):
  print("He are the names of my siblings ", kids[0])

args_function("Emil", "Tobias", "Linus")


def sum_of_numbers(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(sum_of_numbers(1,2,3,4,5))


# Code Challenge

"""
Inside the editor, complete the following steps:
  1. Create a function called greet
  2. Add a parameter called name to the function
  3. Inside the function, print "Hello, " followed by the name parameter
  4. Call the function with the argument "Emil"
"""

def greet(name):
  print("Hello,", name)

greet("Emil")
