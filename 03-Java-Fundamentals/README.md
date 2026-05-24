# 03 — Java Fundamentals

> Learn Java from the ground up — variables, OOP, collections, exception handling, and Maven — building the foundation needed for professional test automation.

---

## Course Overview

Java is the language of enterprise software and Android development. It is also the most common language used in professional QA automation with Selenium and TestNG. This course gives you the Java skills you need to move into Course 04 and beyond.

**Duration:** 4 weeks  
**Effort:** 5–10 hours per week  
**Level:** Beginner (with Python Fundamentals completed)  
**Pre-requisite:** Course 01 — Python Fundamentals

---

## What You Will Learn

- Understand how Java differs from Python
- Write Java programs using correct syntax and structure
- Use all Java primitive data types and the `String` class
- Control program flow with conditionals and loops
- Apply Object-Oriented Programming: classes, objects, inheritance, interfaces
- Use Java Collections: `ArrayList`, `HashMap`, `HashSet`
- Handle exceptions with `try/catch/finally`
- Set up a Maven project in IntelliJ IDEA

---

## Java vs Python — Quick Reference

| Aspect | Python | Java |
|--------|--------|------|
| Typing | Dynamic (no type declaration) | Static (must declare types) |
| Syntax | Simple, minimal punctuation | More verbose, semicolons required |
| File extension | `.py` | `.java` |
| Run command | `python file.py` | `javac File.java` → `java File` |
| OOP | Optional | Core to the language |
| Case sensitive | Yes | Yes |
| Speed | Slower | Faster |

---

## 4-Week Roadmap

### Week 1 — Java Basics & Data Types

| Topic | Key Concepts |
|-------|-------------|
| Java program structure | `public class`, `main` method, `System.out.println()`, semicolons |
| Primitive data types | `int`, `double`, `float`, `boolean`, `char`, `long`, `byte`, `short` |
| Strings | `String` class, `.length()`, `.toUpperCase()`, `.substring()`, `.equals()`, `String.format()` |
| Variables & operators | Arithmetic, comparison, logical, increment/decrement |
| Type casting | Widening (auto), narrowing (manual with cast) |

### Week 2 — Object-Oriented Programming

| Topic | Key Concepts |
|-------|-------------|
| Classes & objects | `class` keyword, `new` keyword, fields, methods |
| Constructors | `__init__` equivalent — called when object is created |
| `this` keyword | Refers to the current instance |
| Access modifiers | `private`, `protected`, `public`, default (package) |
| Encapsulation | Private fields + public getters/setters |
| The 4 OOP pillars | Encapsulation, Inheritance, Polymorphism, Abstraction |

### Week 3 — Inheritance, Interfaces & Collections

| Topic | Key Concepts |
|-------|-------------|
| Inheritance | `extends` keyword, `super`, `@Override` annotation |
| Abstract classes | `abstract` keyword, cannot be instantiated |
| Interfaces | `interface`, `implements`, multiple interfaces allowed |
| `ArrayList` | Dynamic array — `add()`, `remove()`, `get()`, `size()` |
| `HashMap` | Key-value pairs — `put()`, `get()`, `containsKey()` |
| `HashSet` | Unique values — `add()`, `contains()`, `size()` |
| Generics | `List<String>`, `Map<String, Integer>` — type safety |

### Week 4 — Exception Handling & Maven

| Topic | Key Concepts |
|-------|-------------|
| `try / catch / finally` | Handling runtime errors gracefully |
| Common exceptions | `NullPointerException`, `ArrayIndexOutOfBoundsException`, `NumberFormatException` |
| `throws` keyword | Declare checked exceptions on method signatures |
| Custom exceptions | `class MyException extends Exception` |
| Maven | Build tool, `pom.xml`, dependency management |
| Maven commands | `mvn compile`, `mvn test`, `mvn package` |
| IntelliJ IDEA | Project setup, run configurations, debugger |

---

## Setup Instructions

### 1. Install the JDK

Download **Java JDK 17** or later from [oracle.com/java](https://www.oracle.com/java/technologies/downloads/).

Verify installation:
```bash
java -version
javac -version
```

### 2. Install IntelliJ IDEA Community

Download the free Community edition from [jetbrains.com/idea](https://www.jetbrains.com/idea/).

### 3. Create Your First Java Program

```java
// File: HelloWorld.java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

Run it:
```bash
javac HelloWorld.java
java HelloWorld
# Output: Hello, World!
```

---

## Key Java Syntax to Know

```java
// Variables — must declare the type
int age = 21;
double gpa = 3.75;
String name = "Thandi";
boolean isEnrolled = true;

// String comparison — NEVER use == for strings
String a = "hello";
String b = "hello";
System.out.println(a.equals(b));   // true  ✅
System.out.println(a == b);        // unreliable ❌

// Type casting
double price = 9.99;
int rounded = (int) price;          // narrowing — manual cast needed
int count = 5;
double result = count;              // widening — automatic

// for loop
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

// Enhanced for loop
String[] names = {"Thandi", "Sipho", "Ruth"};
for (String n : names) {
    System.out.println(n);
}

// ArrayList
import java.util.ArrayList;
ArrayList<String> list = new ArrayList<>();
list.add("Python");
list.add("Java");
System.out.println(list.get(0));   // Python
```

---

## OOP Example

```java
// Student.java
public class Student {
    private String name;
    private int age;

    // Constructor
    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Getter
    public String getName() {
        return name;
    }

    // Method
    public void introduce() {
        System.out.println("Hi, I am " + name + " and I am " + age + " years old.");
    }
}

// Main.java
public class Main {
    public static void main(String[] args) {
        Student s = new Student("Thandi", 21);
        s.introduce();
        // Output: Hi, I am Thandi and I am 21 years old.
    }
}
```

---

## Assignments

| Assignment | Topics | Marks |
|------------|--------|-------|
| Assignment 1 | Data types, variables, type casting, string methods | 100 |
| Assignment 2 | OOP — create a `Student` class with fields, constructor, and methods | 100 |
| Assignment 3 | Collections — `ArrayList` and `HashMap` operations | 100 |
| Month Project | Library Management System — OOP + collections + exception handling | 100 |

---

## Useful Resources

| Resource | Link |
|----------|------|
| W3Schools Java | [w3schools.com/java](https://www.w3schools.com/java/) |
| Official Java Docs | [docs.oracle.com/javase](https://docs.oracle.com/javase/17/docs/api/) |
| Maven in 5 Minutes | [maven.apache.org/guides/getting-started/maven-in-five-minutes.html](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html) |
| IntelliJ Getting Started | [jetbrains.com/help/idea/getting-started.html](https://www.jetbrains.com/help/idea/getting-started.html) |

---

*Course 3 of 4 — Zinza Institute Of Technology*
