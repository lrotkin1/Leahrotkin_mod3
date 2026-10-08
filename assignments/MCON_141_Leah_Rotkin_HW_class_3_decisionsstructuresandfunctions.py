# MCON 141 — Homework 3
# Class 3 Concepts: if statements and Boolean logic
#
# Name:
# Date:
#
# DIRECTIONS
# 1. Open this file in Pyzo and save it with your own name in the filename.
# 2. Type your solution directly below each exercise's comment block.
# 3. For every exercise that asks for user input, place the input/conversion
#    statements in a try / except ValueError block.
# 4. Test every solution. If you do not use a function, leave comments stating
#    the additional tests you ran, because only the final run is visible.
# 5. All code must run without errors.
#
# EXTRA CREDIT (up to 2 points)
# Write your solutions inside functions where appropriate. For example:
#
# def check_weather(temperature):
#     if temperature > 80:
#         return "It is hot outside."
#     elif temperature < 60:
#         return "It is cold outside."
#     else:
#         return "The weather is mild."
#
# print(check_weather(75))  # should print: The weather is mild.
# print(check_weather(85))  # should print: It is hot outside.
# print(check_weather(50))  # should print: It is cold outside.


# ================================================================
# Exercise 1: What is x relative to y?
#
# Two variables are named x and y. Set y to 10 and x to 20.
#
# Write an if / elif / else statement that compares x and y:
# - If x is less than y, print: "x is less than y"
# - If x is equal to y, print: "x is equal to y"
# - If x is greater than y, print: "x is greater than y"
#
# In a comment within your code, explain the result and why it occurs.
# Also test at least two other values of x and/or y, and document those tests.

y =70
x = 20

if x < y:
    print("x is less than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is greater than y")

'''x is greater than y is what prints since the program runs through first the if and the elif which are both false so then it runs the else which is true'''
'''I ran y as = to 20 so it printed x is equal to y'''
'''I ran y as = to 70 so it printed x is less than y'''

# ================================================================
# Exercise 2: Is x odd or even?
#
# Use x = 20 (or define x again so this exercise runs independently).
#
# If x is even, print: "x is even"
# Otherwise, print: "x is odd"
#
# In a comment within your code, explain the result and why it occurs.
# Test at least one odd value as well.

x = 19

if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")

'''x returns as even since % gives the remainder of the number, and if the remainder is 0 then the number must be even.'''


# ================================================================
# Exercise 3: Polynomials
#
# Two factors, when multiplied together, can produce a binomial.
# Given (x + a) * (x + b), where a and b are integers:
#
#      x + a
#  *   x + b
# -------------
#        xb + ab
#   x^2 + xa
# -------------
#   x^2 + (xb + xa) + ab
#
# Write a program named polynomial that asks the user for integers a and b,
# then computes and prints the expanded binomial.
#
# Example: (x + 2) * (x + 3) = x^2 + 5x + 6
#
# Remember: x^2 means "x squared."
# Use try / except ValueError for user input.

try:
    a = int(input("please give me an integer for a:"))
    b = int(input("please give me an integer for b:"))
    mid = a+b
    constant = a*b
    answer = (f"x^2 + {mid}x + {constant}")
    print(answer)
except ValueError:
    print("You must enter an integer.")


# ================================================================
# Exercise 4: Analyze the polynomial
#
# Given integers a and b, expand (x + a)(x + b) into:
# x^2 + (xb + xa) + ab
#
# Then determine whether:
# - the middle-term coefficient (a + b) is positive, negative, or zero; and
# - the constant (a * b) is positive, negative, or zero.
#
# You may reuse your values of a and b from Exercise 3, but make this exercise
# run independently if possible. Use try / except ValueError for user input.

try:
    a = int(input("please give me an integer for a:"))
    b = int(input("please give me an integer for b:"))
    constant = a*b
    answer = (f"x^2 + {a}x + {b}x {constant}")
    print(answer)
    mid_term = a + b
    if mid_term > 0:
        print("The middle term coefficient is positive")
    elif mid_term < 0:
        print("The middle term coefficient is negative")
    elif mid_term == 0:
        print("The middle term coefficient is zero")
    if constant > 0:
        print("The constant is positive")
    elif constant < 0:
        print("The constant is negative")
    elif constant == 0:
        print("The constant is zero")
except ValueError:
    print("You must enter an integer.")





# ================================================================
# Exercise 5: Explore the and statement
#
# Ask the user to enter integers val1 and val2.
#
# - If both values are positive, print: "val1 and val2 are positive"
#   and print the values.
# - If both values are negative, print: "val1 and val2 are negative"
#   and print the values.
# - Otherwise, print: "The values are not both positive or both negative"
#   and print the values.
#
# Use try / except ValueError for user input.


try:
    val1 = int(input("Please enter a value:"))
    val2 = int(input("Please enter a value:"))
    if val1 > 0 and val2 > 0:
        print("val1 and val2 are positive!")
        print("val1 is", val1)
        print("val2 is", val2)
    elif val1 <0 and val2 < 0:
        print("val1 and val2 are negative!")
        print("val1 is", val1)
        print("val2 is", val2)
    else:
        print("the values are not both positive or both negative")
        print("val1 is", val1)
        print("val2 is", val2)
except ValueError:
    print("You must enter an integer.")



# ================================================================
# Exercise 6: Explore the or statement
#
# Ask the user to enter integers val1 and val2.
#
# - If val1 or val2 is positive, print: "At least one value is positive"
#   and print the values.
# - If val1 or val2 is equal to zero, print: "At least one value is zero"
#   and print the values.
# - Otherwise, print: "At least one value is negative"
#
# Use try / except ValueError for user input.

try:
    val1 = int(input("Enter value for val1:"))
    val2 = int(input("Enter value for val2:"))
    if val1 > 0 or val2 >0:
        print("At least one value is positive")
        print("val1 is", val1)
        print("val2 is", val2)
    elif val1 == 0 or val2 == 0:
        print("At least one value is zero")
        print("val1 is", val1)
        print("val2 is", val2)
    else:
        print("At least one value is negative")
        print("val1 is", val1)
        print("val2 is", val2)
except ValueError:
    print("You must enter an integer.")


# ================================================================
# Exercise 7: Explore not
#
# Set the following variables:
# a = True
# b = True
# c = False
#
# Evaluate and print the results of these expressions:
# 1. not (a and b)
# 2. not a or not c
# 3. not ((a and c) and b)
#
# Include a comment explaining each result.

a = True
b = True
c = False

print(not(a and b))
#since a and b are both true so not a and b is false
print(not a or not c)
#not a is false but not c is true because c is false so because at least one is true so its true
print(not ((a and c) and b))
#a and c is false, b and false is false, and not false is true





# ================================================================
# Exercise 8: Voting Age and Citizenship
#
# Ask the user for their age and whether they are a citizen (yes or no).
#
# - If they are 18 or older AND a citizen, print:
#   "You are eligible to vote."
# - If they are under 18 OR not a citizen, print:
#   "You are not eligible to vote."
#
# Hint: use and for the eligibility requirements. Use try / except ValueError
# for the age input.

try:
    age = int(input("How old are you? "))
    cit = input("Are you a citizen (yes or no): ")
    if age >= 18 and cit == "yes":
        print("You are eligible to vote.")
    elif age < 18 or cit == "no":
        print("Your are not eligible to vote.")
except ValueError:
    print("You must enter a number.")


# ================================================================
# Exercise 9: Number Classification
#
# Ask the user for an integer.
#
# - If it is positive and even, print: "Positive even number."
# - If it is positive and odd, print: "Positive odd number."
# - If it is negative or zero, print: "Not a positive number."
#
# Hint: combine and and or. Use try / except ValueError for user input.

try:
    num = int(input("Enter an integer: "))
    if num >0 and num % 2 == 0:
        print("positive even number")
    elif num > 0 and num % 2 == 1:
        print("positive odd number")
    else:
        print("not a positive number")
except ValueError:
    print("You must enter a number.")


# ================================================================
# Exercise 10: Triangle Check
#
# Ask the user for three side lengths: a, b, and c.
#
# Print "Valid triangle." only if all sides are greater than 0 AND:
# - a + b > c
# - a + c > b
# - b + c > a
#
# Otherwise, print "Not a valid triangle."
#
# Hint: chain multiple and conditions. Use try / except ValueError for input.

try:
    a = int(input("enter length for a: "))
    b = int(input("enter length for b: "))
    c = int(input("enter length for c: "))
    if a > 0 and b> 0 and c > 0 and  a + b > c and a + c > b and b + c > a:
        print("Valid triangle")
    else:
        print("Not a valid triangle")
except ValueError:
    print("You must enter a number.")

# ================================================================
# Exercise 11: Weekend Plan Decision Tree
#
# Ask the user two questions:
# - Is it the weekend? (yes or no)
# - Do you have homework? (yes or no)
#
# Build a decision tree that prints:
# - Weekend and no homework: "Go have fun!"
# - Weekend and homework: "Do your homework first, then relax."
# - Not weekend and homework: "Focus on schoolwork."
# - Not weekend and no homework: "It's a regular day, keep learning!"
#
# Consider converting responses to lowercase so Yes, YES, and yes all work.

week = input("Is it the weekend? (yes or no): ").strip().lower()
hw = input("Do you have homework? (yes or no): ").strip().lower()


if week == "yes" and hw == "no":
    print("Go have fun!")
elif week == "yes" and hw == "yes":
    print("Do your homework first then relax.")
elif week == "no" and hw == "yes":
    print("Focus on schoolwork.")
elif week == "no" and hw == "no":
    print("It's a  regular day, keep learning!")


