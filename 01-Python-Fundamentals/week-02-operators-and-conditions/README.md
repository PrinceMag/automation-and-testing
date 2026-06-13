# Week 2 — Operators and Conditions

## Topics Covered

| File | Topic |
|------|-------|
| `01_operators.py` | Arithmetic, assignment, comparison, logical, membership, identity operators |
| `02_conditions.py` | if / elif / else, nested conditions, inline if, logical operators in conditions |

## How to Run a File

```bash
python 01_operators.py
python 02_conditions.py
```

Or open any file in VS Code and press **F5** to run it.

## Learning Objectives

By the end of this week you should be able to:

- Use all six categories of Python operators
- Understand the difference between `=` (assignment) and `==` (comparison)
- Write `if`, `elif`, and `else` blocks correctly with proper indentation
- Combine conditions using `and`, `or`, and `not`
- Use `in` to check if a value exists in a string or list
- Write a simple inline condition (ternary expression)

## Key Concepts at a Glance

### Operators

| Type | Symbols | Returns |
|------|---------|---------|
| Arithmetic | `+ - * / // % **` | A number |
| Assignment | `= += -= *= /= //= %=` | Updates a variable |
| Comparison | `== != < > <= >=` | `True` or `False` |
| Logical | `and or not` | `True` or `False` |
| Membership | `in not in` | `True` or `False` |
| Identity | `is is not` | `True` or `False` |

### Conditions

```python
# Basic structure
if condition:
    # runs if True
elif another_condition:
    # runs if first was False, this is True
else:
    # runs if nothing above was True

# Inline (ternary)
result = "Pass" if score >= 50 else "Fail"
```

### Common Mistake — Indentation

```python
# ❌ Wrong — no indentation
if age >= 18:
print("Adult")       # IndentationError

# ✅ Correct — 4 spaces inside the block
if age >= 18:
    print("Adult")
```
