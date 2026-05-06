# Loops in Python

i = 1

while i <= 10:
  print("i is being incremented by 1 at a time", i)
  i+=1
  if i == 5:
    continue

# Coding Challenge
  """
  Inside the editor, complete the following steps:
  1. Create a variable i with the value 0
  2. Write a while loop that runs as long as i is less than 6
  3. Inside the loop: increment i by 1
  4. If i equals 3, use continue to skip that iteration
  5. Print i
  """


i = 0
while i < 6:
  i +=1
  if i == 3:
    continue
  print(i)

# For Loop

fruits = ["Apples", "Oranges", "Bananas"]
for fruit in fruits:
  if fruit == "Bananas":
    break
  print(fruit)

# using Range to loop

for x in range(2, 30, 3):
  print(x)

print("===================== NESTED LOOPS ================")

adj = ["Red","big", "tasty"]
softness = ["dry", "soft"]
fruits = ["Apple", "banana", "Cherry"]
count = 0;

for x in adj:
  for y in softness:
    for z in fruits:
      count+=1
      print(x,y, z)

print(count)

"""
Inside the editor, complete the following steps:
1. Create a list called fruits with: "apple", "banana", "cherry"
2. Write a for loop that prints each item in fruits
3. Use break to stop the loop when the item is "banana"
"""
fruits = ["apple", "banana", "cherry"]

for item in fruits:
  if item == "banana":
    break
  print(item)
