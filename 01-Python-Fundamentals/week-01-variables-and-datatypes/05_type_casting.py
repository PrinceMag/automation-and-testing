"""
Topic   : Type Casting (Type Conversion)
File    : 05_type_casting.py
Course  : Python Fundamentals — Week 1
"""

# =========================================================
# WHAT IS TYPE CASTING?
# =========================================================
# Type casting means converting a value from one data type to another.
# Python provides built-in functions to do this.
#
# int()   — converts to integer
# float() — converts to float
# str()   — converts to string
# bool()  — converts to boolean


# =========================================================
# CHECKING THE TYPE OF A VALUE
# =========================================================

name = "Lesedi"
age = 29
height = 1.75
is_enrolled = True

print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_enrolled)) # <class 'bool'>


# =========================================================
# CONVERTING TO INTEGER — int()
# =========================================================

# Convert string to int (string must contain a whole number)
age_as_string = "29"
age_as_int = int(age_as_string)

print(age_as_string)        # 29  — string
print(age_as_int)           # 29  — integer
print(type(age_as_int))     # <class 'int'>

# Convert float to int (decimal part is dropped, not rounded)
price = 99.99
price_as_int = int(price)

print(price_as_int)         # 99 — decimal part removed


# =========================================================
# WHY THIS MATTERS — USER INPUT
# =========================================================
# input() ALWAYS returns a string.
# If the user types a number, you must cast it before doing maths.

# Example:
menu_choice_str = input("Enter menu option (1, 2, or 3): ")

# Compare as string — works when checking exact values
if menu_choice_str == "1":
    print("String comparison: Cappuccino selected")

# Cast to int — works when doing maths or range comparisons
menu_choice_int = int(menu_choice_str)

if menu_choice_int == 1:
    print("Integer comparison: Cappuccino selected")

if menu_choice_int >= 1 and menu_choice_int <= 3:
    print("Valid menu choice entered.")


# =========================================================
# CONVERTING TO FLOAT — float()
# =========================================================

price_input = "49.99"
price = float(price_input)

print(price)                 # 49.99
print(type(price))           # <class 'float'>

# int to float
quantity = 3
quantity_float = float(quantity)
print(quantity_float)        # 3.0


# =========================================================
# CONVERTING TO STRING — str()
# =========================================================
# Use str() when you need to join a number with text using +

student_age = 29
student_name = "Lesedi"

# This would cause a TypeError:
# message = "My name is " + student_name + " and I am " + student_age

# Correct approach — cast to string first:
message = "My name is " + student_name + " and I am " + str(student_age) + " years old."
print(message)

# Better approach — use an f-string (no casting needed):
print(f"My name is {student_name} and I am {student_age} years old.")


# =========================================================
# CONVERTING TO BOOLEAN — bool()
# =========================================================
# Any non-zero number → True
# Zero → False
# Non-empty string → True
# Empty string → False

print(bool(1))       # True
print(bool(0))       # False
print(bool("Hello")) # True
print(bool(""))      # False
print(bool(None))    # False


# =========================================================
# SUMMARY TABLE
# =========================================================

print("\n--- Type Casting Summary ---")

original_str = "100"
original_int = 100
original_float = 100.75

print(f"str to int   : {int(original_str)}")         # 100
print(f"str to float : {float(original_str)}")       # 100.0
print(f"int to str   : {str(original_int)}")         # '100'
print(f"int to float : {float(original_int)}")       # 100.0
print(f"float to int : {int(original_float)}")       # 100  (decimal dropped)
print(f"float to str : {str(original_float)}")       # '100.75'
