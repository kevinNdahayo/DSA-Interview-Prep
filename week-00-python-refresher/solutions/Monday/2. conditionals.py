number = 15

if number > 0:
  print("This number", number, "is greater that zero")

is_logged_in = True

print("============================ Conditionals ===========================")

if is_logged_in:
    print("You can have access to admin dashboard")
    print("You can modify user permissions of certain files")
    print("You can invite other administrators")

a = 33
b = 33

if b > a:
  print(b, "is greater than ", a)
elif a == b:
   print(b, "is equal to ", a)
else:
   print("Find something to do with these numbers", a, b)

score = 20.9999

if score >= 90:
   print("Hullah, You got an A")
elif score >= 80:
   print("You got a B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
else:
   print("This is an automatic F")

print("============================ ShortHand If statement / Ternary Operator for Python ===========================")

age = 5
print("You are old enough to live on your own ") if age > 18 else print ("You are still young, you got", 18 - age, "years to be an adult")

print("============================ Logical Operators (AND, OR, NOT) ===========================")

serieA = 100
serieB = 200
serieC = 300
serieD = 400
if serieA > 1000 and serieB > 400:
  print("Amazing")
else:
   print("Not Amazing at all")

if not serieC > serieD:
   print("Serie C", serieC, " is not greater than Serie D", serieD)

age = 15
has_license = True

if age > 18:
   if has_license:
      print("You can legally drive in USA")
   else:
      print("You can be assisted to learn how to drive")
else:
  if age == 17 or age == 16:
      print("You are too young to drive, but you can get a learner's license")
  elif age >= 14:
    pass # TODO: Implement the logic for this block to work
  else:
    print("You're a baby....")

# Match, Switch case for Python

day = 8

days = 5

match day:
   case 1:
      print("Monday")
   case 2:
      print("Tuesday")
   case 3:
      print("Wednesday")
   case 4:
      print("Thursday")
   case 5:
      print("Friday")
   case 6:
      print("Saturday")
   case 7:
      print("Sunday")
   case _:
      print("Which calendar are you using ? ")

match days:
  case 1 | 2 | 3 | 4 | 5:
    print("These are Week days")
  case _:
    print("Weekend has arrived")

