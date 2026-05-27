"""
Topic   : Numeric Data Types — Integer and Float
File    : 03_numeric_datatypes.py
Course  : Python Fundamentals — Week 1
"""

# =========================================================
# INTEGER (int)
# =========================================================
# An integer is a whole number — no decimal point.
# Use for: age, quantity, count, year, score

student_age = 29
number_of_students = 15
year = 2025

print(student_age)
print(number_of_students)
print(year)
print(type(student_age))    # <class 'int'>


# =========================================================
# FLOAT (float)
# =========================================================
# A float is a number with a decimal point.
# Use for: height, weight, price, temperature, GPA

height = 1.75
weight = 70.5
price = 100.30
temperature = 36.6
gpa = 3.75

print(height)
print(weight)
print(price)
print(type(price))          # <class 'float'>


# =========================================================
# ARITHMETIC OPERATORS
# =========================================================

num1 = 48
num2 = 7

print(num1 + num2)           # 55  — addition
print(num1 - num2)           # 41  — subtraction
print(num1 * num2)           # 336 — multiplication
print(num1 / num2)           # 6.857... — division (always returns float)
print(num1 // num2)          # 6   — floor division (drops decimal)
print(num1 % num2)           # 6   — modulo (remainder after division)
print(num1 ** 2)             # 2304 — exponent (48 to the power of 2)


# =========================================================
# ROUNDING AND PRECISION
# =========================================================

result = num1 / num2
print(result)                # 6.857142857142857
print(round(result, 2))      # 6.86 — rounded to 2 decimal places


# =========================================================
# ORDER OF OPERATIONS (BODMAS)
# =========================================================
# Brackets → Orders (powers) → Division → Multiplication → Addition → Subtraction

calculation = (10 + 5) * 2    # Brackets first: 15 * 2 = 30
print(calculation)            # 30

calculation_2 = 10 + 5 * 2   # Multiplication first: 10 + 10 = 20
print(calculation_2)          # 20


# =========================================================
# REAL-WORLD EXAMPLE — CAFE ORDER TOTAL
# =========================================================

cappuccino_price = 35.00
black_coffee_price = 25.00
quantity = 3

order_total = cappuccino_price * quantity
vat = order_total * 0.15         # 15% VAT
total_with_vat = order_total + vat

print(f"Order total  : R {order_total:.2f}")
print(f"VAT (15%)    : R {vat:.2f}")
print(f"Total to pay : R {total_with_vat:.2f}")
