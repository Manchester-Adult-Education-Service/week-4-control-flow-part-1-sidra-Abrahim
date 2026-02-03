# -------------------------------------------
# Exercise 1: Boolean Logic & Git
# -------------------------------------------
#
# GOAL:
# 1. Master Python Booleans (True/False) and Logic Operators (>, <, ==, !=).
# 2. Practise the Core Git Workflow: Modifying files -> Staging -> Committing -> Pushing.
#
# CONCEPT:
# Boolean logic is the foundation of decision making in code.
# - Comparison: checks values (e.g. x > y)
# - Equality: checks exact matches (e.g. password == "1234")
# - Inequality: checks if things are different (e.g. answer != "wrong")
#
# -------------------------------------------


# -------------------------------------------
# Task 1: Budget Checker (Maths & Logic)
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: Budget Checker\n"
    + "-------------------------------------------")

# TODO:
# 1. Create a variable 'wallet_balance' (integer) and 'item_price' (integer).
# 2. Print a Boolean check to see if you can afford the item.
#    (Hint: You can afford it if your wallet is greater than or equal to the price).
# 3. Create a new variable 'change_available' that is True if you have money left over
#    (wallet is strictly greater than price), and False otherwise. Print this variable.

# Write your code below:
wallet_balance = 20
item_price = 30
change_available = wallet_balance > item_price  


print(f"You can afford the item: {wallet_balance >= item_price} ")
print(f"Change available: {change_available}")

# -------------------------------------------
# Task 2: Security Check (Strings & Inequality)
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Task 2: Security Check\n"
    + "-------------------------------------------")

# TODO:
# 1. Create a variable 'username' and set it to "admin".
# 2. Create a variable 'input_name' and set it to "Admin" (note the capital 'A').
# 3. Print a Boolean check using '==' to see if they match (Notice the result!).
# 4. Print a Boolean check using '!=' (not equal) to confirm they are indeed different strings.

# Write your code below:
username = "admin"
input_name = "Admin"

print(f"The strings match: {username == input_name}")
print(f"The string do not match: {username != input_name}")

# -------------------------------------------
# Task 3: The Bouncer (Input & Types)
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Task 3: The Bouncer\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user for their age using input().
#    (Remember: input() returns a string, so you must wrap it in int()).
# 2. Store a Boolean value in a variable called 'can_enter'.
#    - Set it to True if age is greater than or equal to 18.
# 3. Print: "Access granted: [True/False]" using your variable.

# Write your code below:
age = int(input("Please Enter your age: "))
can_enter = age >= 18

print(f"Access granted: {can_enter}")
# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# You have completed the Core Tasks. Let's save.
# 1. Save this file (Ctrl+S or Cmd+S).
# 2. Open the terminal.
# 3. Run:
#    git add Ex1_boolean.py
#    git commit -m "Completed core boolean tasks"
#    git push origin main
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1: Range Checking (The 'and' Operator)
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 1: Range Checking\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user to enter a number between 1 and 10.
# 2. Check if the number is valid. A valid number is:
#    greater than 0 AND less than or equal to 10.
# 3. Print the result (True if valid, False if invalid).
#
# Hint: You can use: (x > 0) and (x <= 10)

# Write your code below:
number = int(input("Please Enter a number between 1 and 10: "))
valid_num = number > 0 and number <=10 
print(f"Number is valid(between 1 and 10): {valid_num}")


# Extension 2: The "Either/Or" (The 'or' Operator)
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 2: Either/Or Logic\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user for their favourite colour.
# 2. Check if their colour is "Red" OR "Blue".
# 3. Print True if it is one of those, False otherwise.
#
# Hint: Be careful!
# Wrong: if colour == "Red" or "Blue"
# Correct: if colour == "Red" or colour == "Blue"

# Write your code below:
fav_color = input("Please Enter your favourite colour: ")
fav_color = fav_color.upper()
valid_col = fav_color == "RED" or fav_color == "BLUE"

print(f"Your favourite color is either Red or Blue: {valid_col}" )


# Extension 3: Even Number Detector (Modulus %)
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 3: Even Number Detector\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user for a number.
# 2. Use the modulus operator (%) to check if the remainder when dividing by 2 is 0.
# 3. Print True if the number is even, False if odd.
#
# Hint: 5 % 2 gives 1 (Odd). 4 % 2 gives 0 (Even).

# Write your code below:
number = int(input("Please Enter a number: "))
remainder = number % 2
check_even = remainder == 0

print(f"The number is even: {check_even}")
# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# You have completed the Extensions. Let's save.
# 1. Save this file.
# 2. Open the terminal.
# 3. Run:
#    git add Ex1_boolean.py
#    git commit -m "Completed boolean extensions"
#    git push origin main
# -------------------------------------------


# -------------------------------------------
# ADVANCED ACTIVITY: The Leap Year Challenge
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "ADVANCED ACTIVITY: The Leap Year Challenge\n"
    + "-------------------------------------------")

# This is a classic programming interview question!
#
# RULE:
# A year is a leap year if:
# 1. It is divisible by 4...
# 2. ... EXCEPT if it is divisible by 100 (then it is NOT a leap year)...
# 3. ... UNLESS it is ALSO divisible by 400 (then it IS a leap year).
#
# LOGIC SUMMARY:
# (Divisible by 4) AND ((Not divisible by 100) OR (Divisible by 400))
#
# TODO:
# 1. Ask the user to enter a year (integer).
# 2. Create a Boolean variable 'is_leap_year' using the logic above.
# 3. Print "Is leap year: [True/False]"
#
# HINT:
# - Use % for divisible checks (year % 4 == 0)
# - Use != for "not divisible" (year % 100 != 0)
# - Use parenthesis ( ) to group the "OR" part together.

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save this file.
# 2. Run:
#    git add Ex1_boolean.py
#    git commit -m "Completed leap year logic"
#    git push origin main
# -------------------------------------------
