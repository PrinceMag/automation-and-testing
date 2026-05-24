# Assignment 1 — Solutions & Worked Examples

**Course:** Python Fundamentals — Month 1  
**Topic:** Python Variables, Strings & Integers  
**Total Marks:** 100 + 10 bonus

> ⚠️ **Attempt the assignment yourself before reading these solutions.** Use this file to check your work and understand mistakes — not to copy.

---

## Section A — Theory (30 marks)

---

### Q1. What is a Variable in Python? (2 marks)

**Model Answer:**

A variable in Python is a named storage location used to hold a value in memory. You create one by using the `=` operator to assign a value to a name — for example, `age = 21`.

**Key points:**
- Python creates the variable the moment you assign a value to it
- You do not need to declare the data type — Python figures it out automatically
- The `=` sign means **assignment**, not "equals"

```python
name = "Thandi"    # str
age = 21           # int
gpa = 3.75         # float
is_enrolled = True # bool
```

---

### Q2. Multiple Choice (4 marks)

#### Q2a. Which of the following is a VALID Python variable name?

| Option | Valid? | Reason |
|--------|--------|--------|
| `2name` | ❌ | Starts with a digit — not allowed |
| `my_name` | ✅ **CORRECT** | Starts with a letter, uses underscore |
| `my-name` | ❌ | Hyphens are not allowed in variable names |
| `class` | ❌ | Reserved keyword in Python |

**Answer: `my_name`**

---

#### Q2b. What does `print(type(x))` output when `x = 10`?

**Answer: Integer** *(Python actually prints `<class 'int'>` — "Integer" is the intended answer from the options given)*

```python
x = 10
print(type(x))         # <class 'int'>
print(type(x).__name__) # int
```

---

#### Q2c. Which function converts other data types to a string?

**Answer: `str()`**

```python
age = 21
print("I am " + str(age) + " years old")  # I am 21 years old
# Without str() this would throw a TypeError
```

---

#### Q2d. What data type is the value `"3"`?

**Answer: `str`**

> Anything wrapped in quotation marks is a string — even if it looks like a number. `"3"` is a string. `3` is an integer.

```python
print(type("3"))  # <class 'str'>
print(type(3))    # <class 'int'>
```

---

### Q3. True or False (6 marks)

| Statement | Answer | Explanation |
|-----------|--------|-------------|
| Q3a. Variable names are case-sensitive | ✅ **TRUE** | `name` and `Name` are two different variables |
| Q3b. You must declare the type before using a variable | ❌ **FALSE** | Python is dynamically typed — just assign the value |
| Q3c. `.upper()` permanently changes the original variable | ❌ **FALSE** | Strings are immutable — `.upper()` returns a new string |
| Q3d. `int("25")` converts `"25"` to an integer | ✅ **TRUE** | `int()` parses a numeric string into an integer |
| Q3e. A variable name can start with a number | ❌ **FALSE** | Must start with a letter or underscore — `2name` is a `SyntaxError` |
| Q3f. You can reassign a variable to a different data type | ✅ **TRUE** | `x = 5` then `x = "hello"` is perfectly valid in Python |

---

### Q4. What Will This Code Print? (8 marks)

#### Q4a.
```python
name = "Zinza"
print("Hello, " + name + "!")
```
**Output:**
```
Hello, Zinza!
```
*String concatenation joins the three parts with `+`.*

---

#### Q4b.
```python
x = 5
y = 2
print(x * y + 1)
```
**Output:**
```
11
```
*BODMAS: multiply first — `5 × 2 = 10`, then `10 + 1 = 11`.*

---

#### Q4c.
```python
word = "python"
print(word.upper())
```
**Output:**
```
PYTHON
```
*`.upper()` converts every character to uppercase.*

---

#### Q4d.
```python
age = "20"
age = int(age) + 5
print(age)
```
**Output:**
```
25
```
*`int("20")` converts the string to 20, then `20 + 5 = 25`. The result is an integer.*

---

### Q5. Short Answers (10 marks)

#### Q5a. Difference between `int` and `float` (2 marks)

An **integer** (`int`) is a whole number with no decimal point — for example, `age = 25`. A **float** is a number that includes a decimal point — for example, `gpa = 3.75`. Use `int` for counting whole things, and `float` when you need decimal precision (measurements, money, averages).

```python
age = 25        # int
gpa = 3.75      # float

print(type(age))  # <class 'int'>
print(type(gpa))  # <class 'float'>
```

---

#### Q5b. What does `str()` do? (2 marks)

`str()` converts a value of another data type into a string. You would use it when you want to combine a number with text using concatenation (`+`), because Python does not allow you to join a string and an integer directly.

```python
age = 21
# This causes a TypeError:
# print("I am " + age + " years old")

# Correct — use str() to convert:
print("I am " + str(age) + " years old")
# Output: I am 21 years old
```

---

#### Q5c. What is string slicing? (2 marks)

String slicing extracts a portion of a string using index positions in the format `[start:end]`. Indexing starts at `0`. The character at the `end` position is **not** included.

```python
text = "Hello World"
print(text[6:11])  # Output: World
print(text[0:5])   # Output: Hello
print(text[-5:])   # Output: World  (negative indexing from the end)
```

*"World" starts at index 6 and ends before index 11.*

---

#### Q5d. Difference between `=` and `==` (2 marks)

| Operator | Name | Purpose | Example |
|----------|------|---------|---------|
| `=` | Assignment | Stores a value into a variable | `x = 5` — x now holds 5 |
| `==` | Comparison | Checks if two values are equal — returns `True` or `False` | `x == 5` → `True` |

```python
x = 5          # assignment — stores the value 5 in x
print(x == 5)  # comparison — prints True
print(x == 9)  # comparison — prints False
```

---

#### Q5e. Two rules for naming variables (2 marks)

1. **Must start with a letter (a–z, A–Z) or underscore (`_`)** — never a number.
2. **Can only contain letters, numbers, and underscores** — no spaces, hyphens (`-`), or special characters (`@`, `#`, `!`).

**Bonus rule:** Variable names are case-sensitive and cannot be Python reserved keywords (`if`, `for`, `class`, `while`, etc.).

```python
student_name = "valid"  # ✅
_private = "valid"      # ✅
name2 = "valid"         # ✅
2name = "invalid"       # ❌ starts with number
my name = "invalid"     # ❌ space not allowed
my-name = "invalid"     # ❌ hyphen not allowed
```

---

## Section B — Practical (70 marks)

---

### Exercise 1 — Create Your Variables (10 marks)

**Requirements:** Create 5 variables with the exact names shown, using the correct data types, then print each one.

```python
student_name = "Thandi Dlamini"   # str  — use your own name
student_age = 21                   # int  — whole number, no quotes
student_city = "Johannesburg"      # str  — string in quotes
gpa = 3.75                         # float — decimal number
is_enrolled = True                 # bool — True or False, no quotes

print(student_name)   # Thandi Dlamini
print(student_age)    # 21
print(student_city)   # Johannesburg
print(gpa)            # 3.75
print(is_enrolled)    # True
```

**Marking guide (2 marks per variable):**
- Correct variable name spelling — ½ mark
- Correct data type — ½ mark
- Valid value assigned — ½ mark
- Printed correctly — ½ mark

---

### Exercise 2 — String Operations (30 marks)

> Start every answer with: `sentence = "python programming is fun and powerful"`

#### Ex2a — Print in ALL CAPITALS (5 marks)

```python
sentence = "python programming is fun and powerful"
print(sentence.upper())
# Output: PYTHON PROGRAMMING IS FUN AND POWERFUL
```

---

#### Ex2b — Replace a word (5 marks)

```python
sentence = "python programming is fun and powerful"
print(sentence.replace("fun", "amazing"))
# Output: python programming is amazing and powerful
```

> `.replace("old", "new")` finds and replaces all occurrences. The original variable is not changed.

---

#### Ex2c — First 6 characters only (5 marks)

```python
sentence = "python programming is fun and powerful"
print(sentence[0:6])
# Output: python
```

> Index 0 is `p`. `[0:6]` gives characters at positions 0, 1, 2, 3, 4, 5 — which spells `python`.

---

#### Ex2d — Count all characters (5 marks)

```python
sentence = "python programming is fun and powerful"
print(len(sentence))
# Output: 38
```

> `len()` counts every character including spaces.

---

#### Ex2e — Remove extra spaces (5 marks)

```python
messy = "  hello student  "
print(messy.strip())
# Output: hello student
```

> `.strip()` removes leading and trailing whitespace. Use `.lstrip()` for left only, `.rstrip()` for right only.

---

#### Ex2f — Print using an f-string (5 marks)

```python
sentence = "python programming is fun and powerful"
print(f"My sentence is: {sentence}")
# Output: My sentence is: python programming is fun and powerful
```

> f-strings embed variables directly using curly braces `{}`. They are cleaner than concatenation with `+`.

---

### Exercise 3 — Integer Operations (30 marks)

> Start every answer with:
> ```python
> num1 = 48
> num2 = 7
> ```

#### Ex3a — Addition (4 marks)

```python
num1 = 48
num2 = 7
print(num1 + num2)
# Output: 55
```

---

#### Ex3b — Subtraction (4 marks)

```python
num1 = 48
num2 = 7
print(num1 - num2)
# Output: 41
```

---

#### Ex3c — Multiplication (4 marks)

```python
num1 = 48
num2 = 7
print(num1 * num2)
# Output: 336
```

---

#### Ex3d — Division rounded to 2 decimal places (4 marks)

```python
num1 = 48
num2 = 7
print(round(num1 / num2, 2))
# Output: 6.86
```

> `/` always gives a float result. `round(value, 2)` rounds to 2 decimal places.

---

#### Ex3e — Remainder / Modulo (4 marks)

```python
num1 = 48
num2 = 7
print(num1 % num2)
# Output: 6
```

> `48 ÷ 7 = 6 remainder 6`. The `%` operator gives you the remainder only.

---

#### Ex3f — Type conversion (5 marks)

```python
num1 = 48
num2 = 7

num1_str = str(num1)
print(type(num1_str))    # <class 'str'>

num1_back = int(num1_str)
print(type(num1_back))   # <class 'int'>
```

---

#### Ex3g — Even or Odd? (5 marks)

```python
num1 = 48
num2 = 7

if num1 % 2 == 0:
    print(str(num1) + " is even")
else:
    print(str(num1) + " is odd")

# Output: 48 is even
```

> **Logic:** If `num1 % 2 == 0` the remainder when divided by 2 is 0, which means it divides evenly — so it is even.

---

## Section C — Bonus (+ 10 marks)

### Student Profile Program

```python
# Get input from the user
name = input("Enter your name: ")
age  = input("Enter your age: ")
city = input("Enter your city: ")

# Process the data
age  = int(age)          # Convert age from string to integer
name = name.upper()      # Convert name to uppercase

# Print formatted profile
print("")
print("===== STUDENT PROFILE =====")
print(f"Name : {name}")
print(f"Age  : {age}")
print(f"City : {city}")
print("============================")
```

**Sample output:**
```
===== STUDENT PROFILE =====
Name : THANDI DLAMINI
Age  : 21
City : Johannesburg
============================
```

**Mark breakdown:**

| Requirement | Marks |
|-------------|-------|
| `input()` used for name, age, city (1 mark each) | 3 |
| `int()` used to convert age | 1 |
| `.upper()` used on name | 1 |
| f-string used for output | 3 |
| Correct formatting (headers, spacing) | 2 |
| **Total** | **10** |

---

## Common Mistakes to Avoid

```python
# ❌ Cannot concatenate string + integer
print("Hello" + 5)           # TypeError

# ✅ Convert the integer to string first
print("Hello" + str(5))      # Hello5

# ❌ .upper() does NOT change the original variable
name = "thandi"
name.upper()
print(name)                  # thandi — unchanged!

# ✅ Reassign the result
name = name.upper()
print(name)                  # THANDI

# ❌ Variable names cannot start with a number
2name = "Zinza"              # SyntaxError

# ✅
student_name = "Zinza"       # Correct

# ❌ "10" is a string — you cannot do maths on it
x = "10"
print(x + 5)                 # TypeError

# ✅ Cast to int first
print(int(x) + 5)            # 15
```

---

*Zinza Institute Of Technology — Python Fundamentals | Assignment 1 Solutions*
