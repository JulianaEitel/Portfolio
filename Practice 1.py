print("Hello World!")

age = 20
print(age)

# draw a shape:
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

# variables:
character_name = "George"
character_age = "70"
print("There once was a man named " + character_name + " ,")
print("he was " + character_age + " years old.")

character_name = "Paul"
character_age = "85.5"
print("He really liked the name " + character_name + " ,")
print("but didn't like being " + character_age + " years old.")


# strings
print("Giraffe\nAcademy")
phrase = "Giraffe Academy"
print(phrase)
print(phrase + " is cool.")
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(phrase == "Giraffe Academy")
print(len(phrase))
print(phrase[0:6:2])
print(phrase.index("G"))


# numbers
print(3 + 4.5)
print(3 - 4.5)
print(3 * 4.5)
print(3 / 4.5)
print(3 * 4 + 5)
print(3 == 4.5)
print(10 % 3) # remainder of 10/3
my_num = 5
print(str(my_num) + " is an odd number.")

# Functions with numbers
my_num = -5
print(abs(my_num))
print(max(3, 2)) #which number is highest?
print(min(5, 9)) #which number is lowest?
print(round(4.564531, 2))

# imports math modules, access to more functions
# from math import


name = input("Enter your name: ")
age = input(str("Enter your age: "))
print("Hello " + name + "! You are " + age + " years old!")


# Build a calculator
num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
result = float(num1) + float(num2)
print(result)


# Mad Libs Game
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")
print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)


# Lists =[]
friends = ["Kevin", "Jim", "Robert", 2, False]
friends[1] = "Mike"
print(friends)
print(friends[-1])
print(friends[0:3])


# List Functions
lucky_numbers = [15, 42, 4, 16, 32, 8]
friends = ["Kevin", "Robert", "Jim", "Oscar", "Tim", "George"]
friends.extend(lucky_numbers)
friends.append("Milo")
friends.insert(1, "Kelly")
friends.remove("Jim")
friends.pop() #removes last element from list
print(friends.index("Kevin"))
lucky_numbers.sort()
lucky_numbers.reverse()
friends2 = friends.copy()
print(friends2)
friends.clear()

# Tuples =()
coordinates = (4, 5)
print(coordinates[0])


# Functions (def)
def say_hi():   # def + name of function
    print("Hello, User")
say_hi()

def say_hi(name, last_name):
    print("Hello, " + name + last_name)
say_hi("Mike ", "Jones")
say_hi("Steve ", "Harvey")

# Return Statement
def cube(num):
    return num*num*num
result = cube(3)
print(result)


