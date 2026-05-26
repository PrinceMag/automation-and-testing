"""
Topic   : String Data Type
File    : 02_string_datatype.py
Course  : Python Fundamentals — Week 1
"""

# =========================================================
# WHAT IS A STRING?
# =========================================================
# A string is any text enclosed in quotes.
# You can use single quotes, double quotes, or triple quotes.

first_name = "Lesedi"
last_name = 'Dlamini'
greeting = "Hello, World!"

print(first_name)
print(last_name)
print(greeting)


# =========================================================
# MULTI-LINE STRINGS
# =========================================================
# Use triple quotes (""") to write strings that span multiple lines.

menu = """
================= CAFE MENU =================
1. Cappuccino       - R 35.00
2. Black Coffee     - R 25.00
3. White Coffee     - R 30.00
4. Hot Chocolate    - R 40.00
=============================================
"""

system_name = "Lesedi Investment Cafe"

print(system_name)
print(menu)


# =========================================================
# COMMON STRING METHODS
# =========================================================

message = "python programming is fun"

print(message.upper())               # PYTHON PROGRAMMING IS FUN
print(message.capitalize())          # Python programming is fun
print(message.replace("fun", "great"))  # python programming is great
print(message.split(" "))            # ['python', 'programming', 'is', 'fun']
print(len(message))                  # 25 — number of characters including spaces


# =========================================================
# STRING SLICING
# =========================================================
# Access part of a string using [start:end]
# Index starts at 0. The end position is NOT included.

name = "Lesedi Dlamini"

print(name[0])        # L — character at position 0
print(name[0:6])      # Lesedi — positions 0 to 5
print(name[7:])       # Dlamini — from position 7 to end
print(name[-7:])      # Dlamini — last 7 characters (negative index)


# =========================================================
# F-STRINGS (recommended way to build messages)
# =========================================================

student_name = "Lesedi"
student_age = 29

print(f"Hello, my name is {student_name} and I am {student_age} years old.")

# Multi-value f-string
city = "Pretoria"
print(f"Student: {student_name} | Age: {student_age} | City: {city}")


# =========================================================
# USER INPUT
# =========================================================
# input() always returns a STRING, regardless of what the user types.

# Uncomment the lines below to run interactively:

# user_name = input("Enter your name: ")
# print(f"Welcome, {user_name}!")


# =========================================================
# STRING COMPARISON WITH USER INPUT
# =========================================================
# Because input() returns a string, compare it with string values.

menu = """
================= CAFE MENU =================
1. Cappuccino
2. Black Coffee
3. White Coffee
=============================================
"""

print(menu)

menu_choice = input("Enter your choice (1, 2, or 3): ")

# String comparison — compare as strings
if menu_choice == "1":
    print("Enjoy your Cappuccino!")
elif menu_choice == "2":
    print("Enjoy your Black Coffee!")
elif menu_choice == "3":
    print("Enjoy your White Coffee!")
else:
    print("Invalid choice. Please enter 1, 2, or 3.")
