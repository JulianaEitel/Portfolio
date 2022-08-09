# If Statements
is_female = True
is_tall = True

if is_female and is_tall:
    print("You are a tall female")
elif is_female and not(is_tall):
    print("You are a short female")
elif not(is_female) and is_tall:
    print("You are not a female but you are tall")
else:
    print("You are not a female and not tall")


# If Statements & Comparisons   >, <. >=, <=, ==, !=
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(3, 7, 5))


# Building a better calculator
num1 = float(input("Enter first number: "))
op = (input("Enter operator: "))
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")


# Dictionaries  (key:value pairs)
month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
 }
print(month_conversions)
print(month_conversions["Nov"])
print(month_conversions.get("Nov"))
print(month_conversions.get("Luv", "Not a valid key"))

# While Loop
i = 1
while i <= 10:      # keeps printing i as condition is true (i <= 10)
    print(i)
    i += 1          # adds 1 to i
print("Done with loop, condition is met")


# For Loop
for letter in "Python":
    print(letter)

for index in range(3, 10):
    print(index)

friends = ["Jim", "George", "Robert"]
for name in friends:
    print(name)

for index in range(len(friends)):
    print(index)

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first")


# Exponent Function     (take a certain number and raise to a specific power)
print(3**2)

def raise_to_power(base_num, pow_num):      # multiply base_num by itself as many times as pow_num specifies
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(3, 2))


# 2D Lists & Nested Loops
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[0][0])
print(number_grid[2][1])

for row in number_grid:
    print(row)

for row in number_grid:
    for col in row:
        print(col)


# Try / Except
try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")


# Reading Files
employee_file = open("Employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)
print(employee_file.readable())
employee_file.read()
employee_file.readline()    # (first line, if code is run again, second line)
employee_file.close()


# Writing to Files
employee_file = open("employees.txt", "a")  # gets added every time code is run
employee_file.write("\nEmployee 6")
employee_file.close()

employee_file = open("employees_new.txt", "w")
employee_file.write("\nNew Employee 1")
employee_file.close()


# Modules & PIP
# Google: List of Python modules
# PIP to download modules in Terminal: >pip install (module name)
# code: import (module name)
#       (module name).________


# Classes & Objects
from Boarding import Dog
dog1 = Dog("Karlo", "Chihuahua", 4, 9, False)
dog2 = Dog("Chubbs", "English Bulldog", 1, 30, False)
print(dog1.name)
print(dog1.board_with_small_dogs())
print(dog2.board_with_small_dogs())


# Inheritance
from Chef import Chef

myChef = Chef()
myChef.make_special_dish()


from Chef_2 import Chef_2

myChef_2 = Chef_2()
myChef_2.make_salad()
myChef_2.make_special_dish()
myChef_2.make_pasta()



'''
Python Interpreter
On Terminal: 
python3

Accepts code and runs it
'''




















































