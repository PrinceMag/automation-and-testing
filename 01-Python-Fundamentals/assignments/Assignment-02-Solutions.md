# Assignment 2 — Solutions & Worked Examples

**Course:** Python Fundamentals — Week 1  
**Topic:** Python Variables, Data Types & Structure  
**Total Marks:** 100  |  Section A: 50  |  Section B: 50

> ⚠️ **Attempt the assignment yourself before reading these solutions.**  
> Use this file to check your work and understand your mistakes — not to copy answers.

---

## Section A — Theory (50 marks)

---

### Q1. Multiple Choice (20 marks)

| Question | Answer | Why |
|----------|--------|-----|
| Q1a | **C — `first_name`** | Starts with a letter, uses underscore. `2students` starts with a digit. `first-name` uses a hyphen. `first name` has a space. |
| Q1b | **B — PascalCase** | `StudentProfile` — class names always use PascalCase in Python. Variables use snake_case. Constants use UPPER_CASE. |
| Q1c | **C — string** | `input()` always returns a `str`, even if the user types a number like `25`. You must cast it if you need a different type. |
| Q1d | **D — `<class 'float'>`** | `49.99` has a decimal point so it is a float. Python prints `<class 'float'>` when you call `type()` on it. |
| Q1e | **C — `%` (modulo)** | The `%` operator gives the remainder after division. `10 % 3 = 1` because 10 ÷ 3 = 3 remainder **1**. |

---

### Q2. True or False (10 marks)

| Statement | Answer | Explanation |
|-----------|--------|-------------|
| Q2a. Variable names are case-sensitive | ✅ **TRUE** | `name` and `Name` are two completely different variables in Python. |
| Q2b. `bool("")` returns `True` | ❌ **FALSE** | An empty string is "falsy" in Python. `bool("")` returns `False`. Only a non-empty string returns `True`. |
| Q2c. UPPER_CASE is for constants | ✅ **TRUE** | `PI = 3.14` and `MAX_RETRIES = 3` follow the UPPER_CASE constant convention. |
| Q2d. A local variable can be accessed outside its function | ❌ **FALSE** | Local variables only exist while their function is running. Trying to access them outside causes a `NameError`. |
| Q2e. `float("3.14")` works | ✅ **TRUE** | `float()` can convert a string that looks like a decimal number. `float("3.14")` gives `3.14`. |

---

### Q3. Short Answers (20 marks)

---

#### Q3a. Local vs Global Scope (4 marks)

A **global variable** is declared outside any function and can be read from anywhere in the file.  
A **local variable** is declared inside a function and only exists while that function is running — it cannot be accessed from outside.

```python
# Global variable — accessible everywhere
city = "Pretoria"

def get_info():
    # Local variable — only exists inside this function
    street = "123 Lesedi Street"
    print(f"Address: {street}, {city}")   # both accessible here

get_info()
# print(street)   # NameError — street does not exist outside the function
```

---

#### Q3b. Three Variable Naming Rules (4 marks)

**Rule 1: Must start with a letter or underscore — never a digit**

```python
student_name = "Lesedi"   # ✅ correct
_private = "internal"     # ✅ correct
# 2students = "wrong"     # ❌ SyntaxError — starts with digit
```

**Rule 2: No spaces — use underscore to separate words**

```python
first_name = "Lesedi"     # ✅ correct
# first name = "Lesedi"   # ❌ SyntaxError — space not allowed
```

**Rule 3: Only letters, digits, and underscores — no special characters**

```python
course_2_notes = "Week 1" # ✅ correct
# my@name = "Lesedi"      # ❌ SyntaxError — @ not allowed
# my-name = "Lesedi"      # ❌ SyntaxError — hyphen not allowed
```

---

#### Q3c. Three Naming Conventions (4 marks)

| Convention | Used For | Example |
|------------|----------|---------|
| `snake_case` | Variables and functions — words separated by underscore | `first_name`, `get_student_info()` |
| `PascalCase` | Class names — each word starts with a capital letter | `StudentProfile`, `CourseEnrollment` |
| `UPPER_CASE` | Constants — values that never change | `PI = 3.14`, `MAX_RETRIES = 3`, `APP_VERSION = "1.0"` |

---

#### Q3d. Type Casting (4 marks)

Type casting means converting a value from one data type to another using Python's built-in conversion functions: `int()`, `float()`, `str()`, `bool()`.

**String → Integer:**
```python
age_str = "29"
age_int = int(age_str)
print(age_int)          # 29
print(type(age_int))    # <class 'int'>
```

**Integer → String:**
```python
score = 95
score_str = str(score)
print("Your score: " + score_str)   # Your score: 95
print(type(score_str))               # <class 'str'>
```

> The most common reason to cast is because `input()` always returns a string, so you must use `int()` or `float()` before doing maths on user input.

---

#### Q3e. int vs float (4 marks)

An **integer** (`int`) is a whole number with no decimal point.  
A **float** is a number that includes a decimal point.

| Type | Real-World Examples |
|------|-------------------|
| `int` | Age (`age = 29`), number of students (`count = 15`), year (`year = 2025`), quantity in an order (`quantity = 4`) |
| `float` | Price (`price = 49.99`), height (`height = 1.75`), GPA (`gpa = 3.75`), temperature (`temp = 36.6`) |

```python
age = 29            # int  — whole number
price = 249.99      # float — needs decimal precision for money
print(type(age))    # <class 'int'>
print(type(price))  # <class 'float'>
```

---

## Section B — Practical (50 marks)

---

### Exercise 1 — Variables and Naming Conventions (10 marks)

```python
# ── Student Registration Record ──────────────────────────

student_id    = 1001                  # int
student_name  = "Lesedi Dlamini"      # str — use your own name
date_of_birth = "1995-07-14"          # str
course_fee    = 2500.00               # float
is_active     = True                  # bool

print(f"Student ID    : {student_id}")
print(f"Student Name  : {student_name}")
print(f"Date of Birth : {date_of_birth}")
print(f"Course Fee    : R {course_fee:.2f}")
print(f"Active        : {is_active}")
```

**Expected output:**
```
Student ID    : 1001
Student Name  : Lesedi Dlamini
Date of Birth : 1995-07-14
Course Fee    : R 2500.00
Active        : True
```

**Marking guide (2 marks per variable):**
- Correct variable name: ½ mark
- Correct data type: ½ mark
- Valid value assigned: ½ mark
- Printed with f-string and label: ½ mark

---

### Exercise 2 — String Operations (15 marks)

> Base variable used in all tasks:
> ```python
> course_title = "python programming fundamentals"
> ```

#### Ex2a — Title Case (3 marks)

```python
course_title = "python programming fundamentals"
print(course_title.title())
# Output: Python Programming Fundamentals
```

> `.title()` capitalises the first letter of every word.

---

#### Ex2b — Replace a word (3 marks)

```python
course_title = "python programming fundamentals"
print(course_title.replace("fundamentals", "mastery"))
# Output: python programming mastery
```

> `.replace("old", "new")` finds and swaps all occurrences. The original variable is unchanged.

---

#### Ex2c — First 6 characters (3 marks)

```python
course_title = "python programming fundamentals"
print(course_title[0:6])
# Output: python
```

> `[0:6]` returns characters at positions 0, 1, 2, 3, 4, 5.  
> Index starts at 0. Position 6 is not included.

---

#### Ex2d — Character count (3 marks)

```python
course_title = "python programming fundamentals"
print(len(course_title))
# Output: 31
```

> `len()` counts every character including spaces.

---

#### Ex2e — Check if word is in the string (3 marks)

```python
course_title = "python programming fundamentals"
print("python" in course_title)
# Output: True
```

> The `in` keyword checks whether a substring exists inside a string. It returns `True` or `False`.

---

### Exercise 3 — Numeric Operations (15 marks)

> Base variables used in all tasks:
> ```python
> item_price       = 250.00
> quantity         = 4
> discount_percent = 10
> ```

#### Ex3a — Subtotal (3 marks)

```python
item_price = 250.00
quantity = 4
discount_percent = 10

subtotal = item_price * quantity
print(f"Subtotal         : R {subtotal:.2f}")
# Output: Subtotal : R 1000.00
```

---

#### Ex3b — Discount amount (3 marks)

```python
item_price = 250.00
quantity = 4
discount_percent = 10

subtotal = item_price * quantity
discount_amount = subtotal * (discount_percent / 100)
print(f"Discount (10%)   : R {discount_amount:.2f}")
# Output: Discount (10%) : R 100.00
```

---

#### Ex3c — Discounted price (3 marks)

```python
item_price = 250.00
quantity = 4
discount_percent = 10

subtotal = item_price * quantity
discount_amount = subtotal * (discount_percent / 100)
discounted_price = subtotal - discount_amount
print(f"After discount   : R {discounted_price:.2f}")
# Output: After discount : R 900.00
```

---

#### Ex3d — VAT amount (3 marks)

```python
item_price = 250.00
quantity = 4
discount_percent = 10

subtotal = item_price * quantity
discount_amount = subtotal * (discount_percent / 100)
discounted_price = subtotal - discount_amount
vat_amount = discounted_price * 0.15
print(f"VAT (15%)        : R {vat_amount:.2f}")
# Output: VAT (15%) : R 135.00
```

---

#### Ex3e — Final total (3 marks)

```python
item_price = 250.00
quantity = 4
discount_percent = 10

subtotal         = item_price * quantity
discount_amount  = subtotal * (discount_percent / 100)
discounted_price = subtotal - discount_amount
vat_amount       = discounted_price * 0.15
final_total      = discounted_price + vat_amount

print(f"Final Total      : R {round(final_total, 2):.2f}")
# Output: Final Total : R 1035.00
```

**Full calculation walkthrough:**
```
subtotal         = 250.00 × 4       = 1000.00
discount_amount  = 1000.00 × 10%    = 100.00
discounted_price = 1000.00 - 100.00 = 900.00
vat_amount       = 900.00 × 15%     = 135.00
final_total      = 900.00 + 135.00  = 1035.00
```

---

### Exercise 4 — Booleans and Type Casting (15 marks)

#### Ex4a — Boolean conditional check (5 marks)

```python
has_paid        = True
is_enrolled     = True
has_id_document = False

if has_paid and is_enrolled and has_id_document:
    print("Access granted. Welcome to class.")
else:
    print("Access denied. Please check your requirements.")

# Output: Access denied. Please check your requirements.
```

> `has_id_document` is `False`, so the `and` condition fails — all three must be `True` for access.

---

#### Ex4b — Type casting + comparison (5 marks)

```python
user_age = "25"

age = int(user_age)   # cast string "25" to integer 25

if age >= 18:
    print("You are eligible.")
else:
    print("You are not eligible.")

# Output: You are eligible.
```

> Without `int()`, `"25" >= 18` would raise a `TypeError` because you cannot compare a string to an integer.

---

#### Ex4c — Mini registration program using input() (5 marks)

```python
name = input("Enter your name: ")
age  = input("Enter your age: ")

age  = int(age)          # cast age from string to integer
name = name.upper()      # convert name to uppercase

print(f"Welcome {name}, you are {age} years old.")
```

**Sample run:**
```
Enter your name: Lesedi
Enter your age: 29
Welcome LESEDI, you are 29 years old.
```

---

### Exercise 5 — Scope and Code Structure (10 marks)

#### Ex5a — Local and Global Scope (5 marks)

```python
# Global constant — accessible everywhere in the file
INSTITUTION_NAME = "Zinza Institute Of Technology"

def get_student_info():
    # Local variable — only exists inside this function
    student_name = "Lesedi Dlamini"

    print(f"Institution  : {INSTITUTION_NAME}")   # global
    print(f"Student Name : {student_name}")        # local

# Call the function
get_student_info()
```

**Output:**
```
Institution  : Zinza Institute Of Technology
Student Name : Lesedi Dlamini
```

> If you try `print(student_name)` outside the function you will get a `NameError`.  
> `INSTITUTION_NAME` works everywhere because it is global.

---

#### Ex5b — Class using PascalCase (5 marks)

```python
class CourseEnrollment:
    """Represents a student's enrollment in a course."""

    def __init__(self, student_name, course_name, fee):
        self.student_name = student_name   # instance variable
        self.course_name  = course_name    # instance variable
        self.fee          = fee            # instance variable

    def print_enrollment(self):
        print("─── Enrollment Details ───────────────")
        print(f"Student : {self.student_name}")
        print(f"Course  : {self.course_name}")
        print(f"Fee     : R {self.fee:.2f}")
        print("──────────────────────────────────────")


# Create one object and call the method
enrolment = CourseEnrollment("Lesedi Dlamini", "Python Fundamentals", 2500.00)
enrolment.print_enrollment()
```

**Output:**
```
─── Enrollment Details ───────────────
Student : Lesedi Dlamini
Course  : Python Fundamentals
Fee     : R 2500.00
──────────────────────────────────────
```

**Key points:**
- Class name `CourseEnrollment` uses **PascalCase**
- `__init__` is the constructor — it runs automatically when you create an object
- `self` refers to the specific object being created
- Instance variables (`self.student_name`) belong to each individual object

---

## Common Mistakes to Avoid

```python
# ❌ Cannot do maths on a string from input()
age = input("Enter age: ")
print(age + 5)              # TypeError

# ✅ Cast to int first
age = int(input("Enter age: "))
print(age + 5)              # works correctly


# ❌ Thinking .replace() changes the original
course = "python fundamentals"
course.replace("python", "java")
print(course)               # still "python fundamentals"

# ✅ Reassign the result
course = course.replace("python", "java")
print(course)               # "java fundamentals"


# ❌ Confusing = (assignment) with == (comparison)
x = 10
if x = 10:                  # SyntaxError
    print("ten")

# ✅
if x == 10:
    print("ten")


# ❌ Accessing a local variable outside its function
def my_function():
    message = "hello"

my_function()
print(message)              # NameError

# ✅ Return the value or use a global variable
def my_function():
    message = "hello"
    return message

result = my_function()
print(result)               # hello
```

---

## Marking Summary

| Section | Question | Topic | Marks |
|---------|----------|-------|-------|
| A | Q1a–e | Multiple Choice | 20 |
| A | Q2a–e | True or False | 10 |
| A | Q3a–e | Short Answers | 20 |
| B | Ex 1 | Variables + f-strings | 10 |
| B | Ex 2a–e | String operations | 15 |
| B | Ex 3a–e | Numeric operations | 15 |
| B | Ex 4a–c | Booleans + type casting | 15 |
| B | Ex 5a–b | Scope + class structure | 10 |
| | | **Total** | **100** |

---

*Zinza Institute Of Technology — Python Fundamentals | Week 1 | Assignment 2 Solutions*
