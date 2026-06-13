"""
Topic   : Operators
File    : 07_operators.py
Course  : Python Fundamentals — Week 1
"""

# =========================================================
# WHAT IS AN OPERATOR?
# =========================================================
# An operator is a symbol that performs an operation on values.
# Python has 6 categories of operators:
#
#   1. Arithmetic   — do maths
#   2. Assignment   — store values
#   3. Comparison   — compare two values (returns True/False)
#   4. Logical      — combine conditions (and, or, not)
#   5. Membership   — check if a value exists (in, not in)
#   6. Identity     — check if two variables point to the same object (is, is not)


# =========================================================
# 1. ARITHMETIC OPERATORS
# =========================================================
# Used to perform mathematical calculations.

a = 20
b = 6

print(a + b)    # 26  — addition
print(a - b)    # 14  — subtraction
print(a * b)    # 120 — multiplication
print(a / b)    # 3.333... — division (always returns float)
print(a // b)   # 3   — floor division (removes decimal, rounds DOWN)
print(a % b)    # 2   — modulo (remainder after division)
print(a ** 2)   # 400 — exponent (20 to the power of 2)

# Real-world example — Cafe receipt
item_price = 35.00
quantity   = 3
vat_rate   = 0.15

subtotal   = item_price * quantity        # 105.00
vat        = subtotal * vat_rate          # 15.75
total      = subtotal + vat               # 120.75

print(f"Subtotal : R {subtotal:.2f}")
print(f"VAT      : R {vat:.2f}")
print(f"Total    : R {total:.2f}")


# =========================================================
# 2. ASSIGNMENT OPERATORS
# =========================================================
# Used to assign or update the value of a variable.

score = 10          # basic assignment

score += 5          # same as: score = score + 5   →  15
print(score)        # 15

score -= 3          # same as: score = score - 3   →  12
print(score)        # 12

score *= 2          # same as: score = score * 2   →  24
print(score)        # 24

score //= 4         # same as: score = score // 4  →  6
print(score)        # 6

score **= 2         # same as: score = score ** 2  →  36
print(score)        # 36

score %= 10         # same as: score = score % 10  →  6
print(score)        # 6

# Common use — running total in an order
cart_total = 0.00
cart_total += 35.00     # add cappuccino
cart_total += 49.99     # add muffin
cart_total += 15.00     # add juice
print(f"Cart total: R {cart_total:.2f}")   # R 99.99


# =========================================================
# 3. COMPARISON OPERATORS
# =========================================================
# Compare two values and always return True or False.

x = 10
y = 20

print(x == y)   # False — equal to
print(x != y)   # True  — not equal to
print(x < y)    # True  — less than
print(x > y)    # False — greater than
print(x <= 10)  # True  — less than or equal to
print(x >= 10)  # True  — greater than or equal to

# Common use — checking age for access
age = 17
print(age >= 18)    # False — not old enough

# Comparing strings
name = "Lesedi"
print(name == "Lesedi")     # True
print(name == "lesedi")     # False — case-sensitive!
print(name != "Sipho")      # True


# =========================================================
# 4. LOGICAL OPERATORS
# =========================================================
# Combine multiple conditions together.
# Returns True or False.

# AND — BOTH conditions must be True
has_ticket = True
has_id     = True
print(has_ticket and has_id)    # True — both are True

has_ticket = True
has_id     = False
print(has_ticket and has_id)    # False — one is False

# OR — AT LEAST ONE condition must be True
is_student    = False
has_discount  = True
print(is_student or has_discount)   # True — at least one is True

is_student    = False
has_discount  = False
print(is_student or has_discount)   # False — both are False

# NOT — flips the boolean
is_closed = False
print(not is_closed)    # True  — the shop IS open
print(not True)         # False
print(not False)        # True

# Combined example — access control
age        = 20
has_card   = True
is_banned  = False

can_enter = (age >= 18) and has_card and (not is_banned)
print(can_enter)    # True — all conditions pass


# =========================================================
# 5. MEMBERSHIP OPERATORS
# =========================================================
# Check whether a value EXISTS inside a sequence (string, list, etc.)
# Returns True or False.

# in — checks if value is present
menu_items = ["Cappuccino", "Black Coffee", "White Coffee"]
print("Cappuccino" in menu_items)       # True
print("Espresso" in menu_items)         # False

course_title = "python programming fundamentals"
print("python" in course_title)         # True
print("java" in course_title)           # False

# not in — checks if value is NOT present
blocked_users = ["admin", "root", "test"]
username = "lesedi"
print(username not in blocked_users)    # True — lesedi is not blocked


# =========================================================
# 6. IDENTITY OPERATORS
# =========================================================
# Check whether two variables point to the SAME object in memory.
# Different from == which checks if values are equal.

x = [1, 2, 3]
y = x           # y points to the SAME list as x
z = [1, 2, 3]   # z is a NEW list with the same values

print(x is y)   # True  — same object in memory
print(x is z)   # False — different objects (same values, different location)
print(x == z)   # True  — values are equal (== checks content)

# Most common use — checking for None
name = None
print(name is None)       # True  — correct way to check for None
print(name is not None)   # False
