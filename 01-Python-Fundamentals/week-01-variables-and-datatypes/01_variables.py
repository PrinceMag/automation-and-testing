"""
Topic   : Variables
File    : 01_variables.py
Course  : Python Fundamentals — Week 1
"""

# =========================================================
# WHAT IS A VARIABLE?
# =========================================================
# A variable is a named storage location that holds a value.
# Python creates the variable the moment you assign a value to it.
# You do NOT need to declare its type first.

first_name = "Lesedi"
age = 29
height = 1.75
is_enrolled = True


# =========================================================
# VARIABLE NAMING RULES
# =========================================================

# RULE 1: Must start with a letter or underscore — never a number
student_name = "Lesedi"    # correct
_private_name = "Lesedi"   # correct — underscore prefix is valid
# 1student = "Lesedi"      # SyntaxError — starts with a digit

# RULE 2: Numbers are allowed in the middle or at the end
student1 = "Lesedi"        # correct
course_2_notes = "Week 1"  # correct

# RULE 3: No spaces — use underscore instead
first_name = "Lesedi"      # correct
# first name = "Lesedi"    # SyntaxError — space not allowed

# RULE 4: Only letters, digits, and underscores allowed
my_variable = "valid"      # correct
# my-variable = "valid"    # SyntaxError — hyphen not allowed
# my@variable = "valid"    # SyntaxError — special character not allowed

# RULE 5: Python is case-sensitive
name = "Lesedi"
Name = "Sipho"             # These are TWO different variables
print(name)                # Lesedi
print(Name)                # Sipho


# =========================================================
# PYTHON NAMING CONVENTIONS
# =========================================================

# snake_case — used for variables and functions (words separated by _)
first_name = "Lesedi"
student_age = 29
total_price = 100.50

# PascalCase — used for class names (each word starts with capital)
# StudentProfile
# CafeOrderSystem
# InvoiceManager

# UPPER_CASE — used for constants (values that never change)
MAX_RETRIES = 3
PI = 3.14159
APP_VERSION = "1.0.0"

# Private convention — single underscore prefix means "internal use"
_internal_id = 1001


# =========================================================
# RESERVED WORDS (cannot be used as variable names)
# =========================================================
# These words belong to Python and cannot be used as variable names:
# if, else, elif, for, while, def, class, return, import, from,
# True, False, None, and, or, not, in, is, pass, break, continue

# Workaround when a name clashes with a reserved word:
# Add a trailing underscore
class_ = "Python Fundamentals"   # class is reserved, so use class_
type_ = "integer"                 # type is a built-in, so use type_


# =========================================================
# PRINTING VARIABLES
# =========================================================

student_name = "Lesedi"
student_age = 29
student_city = "Pretoria"

print(student_name)
print(student_age)
print(student_city)

# Using f-string to print with labels (cleaner than concatenation)
print(f"Name : {student_name}")
print(f"Age  : {student_age}")
print(f"City : {student_city}")
