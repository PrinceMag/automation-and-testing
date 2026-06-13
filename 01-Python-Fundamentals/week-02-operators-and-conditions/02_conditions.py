"""
Topic   : Conditions (if / elif / else)
File    : 08_conditions.py
Course  : Python Fundamentals — Week 1
"""

# =========================================================
# WHAT ARE CONDITIONS?
# =========================================================
# Conditions let your programme make decisions.
# Python uses if, elif, and else to control which code runs.
#
# Structure:
#   if <condition is True>:
#       run this code
#   elif <another condition is True>:
#       run this code instead
#   else:
#       run this if nothing above was True
#
# IMPORTANT: Python uses INDENTATION (4 spaces) to show which
# code belongs inside an if block. Indentation is not optional.


# =========================================================
# BASIC if STATEMENT
# =========================================================
# Runs the block only if the condition is True.

age = 20

if age >= 18:
    print("You are an adult.")

# If the condition is False, nothing happens
age = 15

if age >= 18:
    print("This will NOT print.")


# =========================================================
# if / else STATEMENT
# =========================================================
# Run one block if True, a different block if False.

age = 16

if age >= 18:
    print("Access granted.")
else:
    print("Access denied. You must be 18 or older.")

# Output: Access denied. You must be 18 or older.


# =========================================================
# if / elif / else STATEMENT
# =========================================================
# Use elif to check multiple conditions one by one.
# Python checks each condition in order and runs the FIRST one that is True.
# Once a match is found, it skips the rest.

score = 75

if score >= 90:
    print("Grade: A — Distinction")
elif score >= 80:
    print("Grade: B — Merit")
elif score >= 70:
    print("Grade: C — Pass")
elif score >= 50:
    print("Grade: D — Below Average")
else:
    print("Grade: F — Fail")

# Output: Grade: C — Pass


# =========================================================
# REAL-WORLD EXAMPLE — CAFE ORDER SYSTEM
# =========================================================

menu = """
======== LESEDI INVESTMENT CAFE ========
  1. Cappuccino     — R 35.00
  2. Black Coffee   — R 25.00
  3. White Coffee   — R 30.00
  4. Hot Chocolate  — R 40.00
========================================
"""

print(menu)
choice = input("Enter your choice (1-4): ")

if choice == "1":
    print("Order placed: Cappuccino — R 35.00")
elif choice == "2":
    print("Order placed: Black Coffee — R 25.00")
elif choice == "3":
    print("Order placed: White Coffee — R 30.00")
elif choice == "4":
    print("Order placed: Hot Chocolate — R 40.00")
else:
    print("Invalid choice. Please enter a number between 1 and 4.")


# =========================================================
# COMPARISON OPERATORS IN CONDITIONS
# =========================================================

temperature = 18

if temperature > 30:
    print("It is hot today.")
elif temperature > 20:
    print("It is warm today.")
elif temperature > 10:
    print("It is cool today.")
else:
    print("It is cold today.")

# Output: It is cool today.


# =========================================================
# LOGICAL OPERATORS IN CONDITIONS
# =========================================================
# Combine multiple conditions using and, or, not.

# AND — both must be True
username = "lesedi"
password = "abc123"

if username == "lesedi" and password == "abc123":
    print("Login successful.")
else:
    print("Incorrect username or password.")

# OR — at least one must be True
is_weekend  = False
is_holiday  = True

if is_weekend or is_holiday:
    print("The cafe is open for extended hours!")
else:
    print("Normal business hours apply.")

# NOT — flips the condition
is_logged_in = False

if not is_logged_in:
    print("Please log in to continue.")


# =========================================================
# NESTED CONDITIONS
# =========================================================
# A condition inside another condition.
# Be careful not to nest too deeply — it becomes hard to read.

age      = 22
has_card = True

if age >= 18:
    if has_card:
        print("Entry allowed. Card payment accepted.")
    else:
        print("Entry allowed. Cash payment only.")
else:
    print("Entry not allowed. Must be 18 or older.")


# =========================================================
# CHECKING USER INPUT — INTEGER vs STRING
# =========================================================
# input() returns a STRING.
# You need int() if you want to compare numerically.

# String comparison (works for exact match only)
choice = input("Enter a number (1-3): ")

if choice == "1":
    print("You chose option 1.")

# Integer comparison (needed for range checks like >= or <=)
choice_int = int(choice)

if choice_int >= 1 and choice_int <= 3:
    print("Valid option selected.")
else:
    print("Please enter a number between 1 and 3.")


# =========================================================
# MEMBERSHIP OPERATOR in CONDITIONS
# =========================================================

allowed_users = ["lesedi", "thandi", "sipho"]
username = input("Enter your username: ")

if username in allowed_users:
    print(f"Welcome back, {username}!")
else:
    print("Username not found. Please register first.")


# =========================================================
# INLINE if (TERNARY EXPRESSION)
# =========================================================
# A shorthand for simple if/else on one line.
# Format:  value_if_true  if  condition  else  value_if_false

age = 20
status = "adult" if age >= 18 else "minor"
print(status)   # adult

# Another example
score = 65
result = "Pass" if score >= 50 else "Fail"
print(f"Result: {result}")   # Result: Pass


# =========================================================
# SUMMARY — WHEN TO USE EACH
# =========================================================
#
#  if only             → you only care when condition is True
#  if / else           → two possible outcomes (True or False)
#  if / elif / else    → three or more possible outcomes
#  nested if           → second decision depends on first
#  inline if           → simple one-line assignment based on condition
#  and / or / not      → combine or flip conditions
#
# =========================================================
