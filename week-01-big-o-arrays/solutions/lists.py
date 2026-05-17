nums = [1, 2, 3, 4, 5]
mixed = [1, "Hello", True]
empty = []

print(nums[0])
print(nums[1])
print(nums[2])
print(nums[-1])
print(len(nums))

# Update elements in our List
nums[1] = 1

print("===========================================")
print(nums[1])

print("===========================================")
print("Looping Through the List")
for num in nums:
    print(num)

print("===========================================")
print("Num of elem in the List")
print(len(nums))

print("===========================================")
print("Looping Through the List")
for num in nums:
    print(num)

print("===========================================")
print("Index Looping using Range function")

x = range(3, 10)

for single_number in x:
    print(single_number)

print("===========================================")
print("Index Looping using Range function of nums list")
for numbers_in_num in range(len(nums)):
    print(numbers_in_num, nums[numbers_in_num])

print("===========================================")
print("Appending Elements in Lists")
nums.append(19)
nums.append(20)
nums.append(30)

for i in range(len(nums)):
    print(nums[i])

# The time complexity for Append here is O(1)

print("===========================================")
print("Insert Elements in Lists")

fruits = ["apple", "banana", "cherry"]

# Insert Mango as the second index element in the list

fruits.insert(0, "Mango")

for fruit in range(len(fruits)):
    print(fruits[fruit])

# Insert Operation takes O(n) time complexity

print("===========================================")
print("Removing Elements in Lists: Pop")

fruits.pop()

for i in range(len(fruits)):
    print(fruits[i])

# The pop method here takes O(n) time complexity


print("===========================================")
print("Removing Elements in Lists using remove")

print("===========================================")
print("Before using remove operator: Lists")

fruits.remove("banana")

for i in range(len(fruits)):
    print(fruits[i])

# Time complexity for remove operator for lists is O(n)

print("===========================================")
print("Slicing in Python")

a = [1,2,3,4,5,6,7,8,9]

# Get all the elements in the list using Python Slicing
print(a[::])
print(a[:])

# Slicing takes the start parameter which is the starting index up to ending index exclusively (meaning ending index is excluded)
print(a[1:4]) # we should be able to print 2, 3, 4
print(a[1:1]) # we should be able to print

# Get all the items after 2nd position
print(a[1:])

# Negative slicing
print(a[:-2])

# Reverse a list using slicing techniques

print(a[::-1])

# Summary on Slicing
# -> First 3 elements
print(a[::3])

# -> From Index 3 onwords
print(a[3::])

# -> Last 2 elements
print(a[-2::])

#-> Reverse the whole list
print(a[::-1])

print("===========================================")
print("Sorting elements in Python")

elems = [40,50,30, 100, 200, 80]

sorted_elems = sorted(elems)

print(sorted_elems)

