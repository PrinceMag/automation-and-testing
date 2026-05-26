"""
Topic   : Boolean Data Type
File    : 04_boolean_datatype.py
Course  : Python Fundamentals — Week 1
"""

# =========================================================
# WHAT IS A BOOLEAN?
# =========================================================
# A boolean holds one of two values: True or False.
# Note: True and False must start with a capital letter in Python.

is_enrolled = True
is_graduated = False

print(is_enrolled)        # True
print(is_graduated)       # False
print(type(is_enrolled))  # <class 'bool'>


# =========================================================
# REAL-WORLD USE CASES FOR BOOLEANS
# =========================================================
# Booleans are used whenever you need to check a YES/NO condition.

is_logged_in = True
is_admin = False
is_available = True
has_paid = False
door_is_locked = True
oven_is_on = False
tank_is_full = True
is_clean = False
is_open = True
is_cold = False


# =========================================================
# BOOLEANS FROM COMPARISONS
# =========================================================
# Comparison operators return a boolean result.

age = 18
print(age >= 18)    # True  — age is greater than or equal to 18
print(age == 21)    # False — age is not 21
print(age != 21)    # True  — age is not equal to 21
print(age < 10)     # False — age is not less than 10


# =========================================================
# BOOLEANS IN IF STATEMENTS
# =========================================================

is_enrolled = True

if is_enrolled:
    print("Student has access to course material.")
else:
    print("Student is not enrolled.")


# =========================================================
# COMBINING BOOLEANS — and / or / not
# =========================================================

has_id = True
has_paid = True

# and — BOTH conditions must be True
if has_id and has_paid:
    print("Access granted.")

# or — AT LEAST ONE condition must be True
has_discount_card = False
is_student = True

if has_discount_card or is_student:
    print("Discount applied.")

# not — flips the boolean
door_is_locked = True
print(not door_is_locked)    # False — the door is NOT locked


# =========================================================
# REAL-WORLD EXAMPLE — CAFE ORDER SYSTEM
# =========================================================

is_open = True
table_available = True
customer_has_paid = False

if is_open and table_available:
    print("Welcome! A table is ready for you.")
else:
    print("Sorry, we are closed or fully booked.")

if not customer_has_paid:
    print("Please proceed to the till to pay.")
