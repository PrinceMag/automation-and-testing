"""
Topic   : Scope and Python Code Structure
File    : 06_scope_and_structure.py
Course  : Python Fundamentals — Week 1
"""

# =========================================================
# PYTHON CODE STRUCTURE
# =========================================================
# A Python programme is made up of:
#   - Variables     — store data
#   - Functions     — reusable blocks of code (def)
#   - Classes       — blueprints for objects (class)
#
# Naming convention reminder:
#   snake_case   → variables and functions
#   PascalCase   → classes
#   UPPER_CASE   → constants

APP_NAME = "Lesedi Investment System"    # constant
version = "1.0.0"                        # variable


# =========================================================
# SCOPE — LOCAL vs GLOBAL
# =========================================================

# GLOBAL SCOPE
# Variables declared outside any function or class.
# They can be read from anywhere in the file.

city = "Pretoria"        # global variable
province = "Gauteng"     # global variable


def get_location():
    # LOCAL SCOPE
    # Variables declared inside a function.
    # They only exist while the function is running.
    # They cannot be accessed from outside the function.
    street = "123 Lesedi Street"        # local variable
    return f"{street}, {city}, {province}"


print(get_location())
# print(street)   # NameError — street only exists inside get_location()


# =========================================================
# REAL-WORLD SCOPE EXAMPLE — COMPOUND ANALOGY
# =========================================================
# Think of scope like a compound (yard) and the rooms inside it.
# The yard (global) can be seen by everyone.
# Each room (function) has its own private contents.

# Global — visible to the whole file
compound_address = "1234 Lesedi Street, Pretoria"

def get_house_details():
    # Local — only visible inside this function
    house_number = "Unit 3"
    house_type = "Townhouse"
    return f"{house_number} — {house_type} at {compound_address}"

def get_car():
    # Local — only visible inside this function
    car_model = "BMW 3 Series"
    car_colour = "White"
    return f"{car_colour} {car_model}"

print(get_house_details())
print(get_car())


# =========================================================
# CLASS STRUCTURE (PascalCase naming)
# =========================================================

class StudentProfile:
    """
    Represents a student enrolled in a course.
    PascalCase is used for class names.
    """

    # Class-level constant (shared by all instances)
    INSTITUTION = "Zinza Institute Of Technology"

    def __init__(self, name, age, city):
        # Instance variables — unique to each student object
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        """Prints a formatted introduction for this student."""
        print(f"Name        : {self.name}")
        print(f"Age         : {self.age}")
        print(f"City        : {self.city}")
        print(f"Institution : {self.INSTITUTION}")
        print()


# Create two student objects from the same class
student_one = StudentProfile("Lesedi Dlamini", 29, "Pretoria")
student_two = StudentProfile("Thandi Nkosi", 22, "Johannesburg")

student_one.introduce()
student_two.introduce()


# =========================================================
# RESERVED WORD WORKAROUNDS
# =========================================================
# Python has reserved words that cannot be used as variable names.
# When a name clashes with a reserved word, add a trailing underscore.

class CourseDetails:
    class_ = "Python Fundamentals"   # 'class' is reserved → use class_
    type_ = "Beginner"               # 'type' is a built-in → use type_

    def get_details(self):
        return f"{self.class_} — {self.type_}"

course = CourseDetails()
print(course.get_details())
