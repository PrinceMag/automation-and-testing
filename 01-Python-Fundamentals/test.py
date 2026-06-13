# # Variable naming convention

# # 1. Cannot start with a number

# # 1name = "Prince"
# name1 = "Prince"
# name2  = "Lesedi"

# # 2. Cannot contain spaces , use an underscore to separate the wording
# name_1 = "Prince"

# # 3. Cannot contain special characters except an underscore _

# # name-1 = "Prince"
# name_1  =  "Prince"
# # name=1 = "Prince"


# # a = b, b = c therefore a = c

# c = 1

# a=b=c
# print(a)

# # 1.


# x = float(input())

# print(type(x))

"""
Create the following 5 variables using the EXACT names shown:

  student_id     → int    (e.g. 1001)
  student_name   → str    (your full name)
  date_of_birth  → str    (e.g. "2000-03-15")
  course_fee     → float  (e.g. 2500.00)
  is_active      → bool   (True or False)

After creating all 5 variables, print each one using an f-string with a label.
Example: print(f"Student ID : {student_id}")
"""

# student_id = 97
# student_name = "Lesedi"
# date_of_birth = "1997-02-11"
# course_fee = 30_000
# is_active = False

# resu`lt =f"""
# My student id is {student_id}
# My student name is {student_name}
# My date of birth is {date_of_birth}
# My course fee is {course_fee}
# My active status is {is_active}
# """

# print(result)`

course_title = "python programming fundamentals"
# print(course_title.title())
# print(course_title.replace("fundamentals", "mastery"))

# print(len(course_title))

"""
Use these variables for all tasks:
  item_price = 250.00
  quantity = 4
  discount_percent = 10

Start every answer block with those three lines.
"""

item_price = 250.00
quantity = 4
discount_percent = 10
subtotal = item_price * quantity

# print(subtotal)  #  Expected: 1000.0

# discount_amount = subtotal * (discount_percent / 100)  # Expected: 100.0
# print(discount_amount)

"""
Ex4c. Write a mini registration program using input(). (5 marks)

Write a program that:
(i)   Asks for name using input()
(ii)  Asks for age using input()
(iii) Converts age to integer
(iv)  Converts name to UPPERCASE
(v)   Prints: "Welcome [NAME], you are [AGE] years old." using an f-string
"""

name = input("Enter your name: ")
print("My name is " + name)