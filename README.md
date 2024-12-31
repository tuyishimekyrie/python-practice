# **Python Basics 101**

![Python Logo](https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg)

A beginner-friendly guide to learning the basics of Python programming. This repository contains concise examples and explanations to help you get started.

---

## **Table of Contents**

1. [What is Python?](#what-is-python)
2. [How Can Python Be Used?](#how-can-python-be-used)
3. [Key Concepts Covered](#key-concepts-covered)
   - [Variables](#variables)
   - [Type Annotations](#type-annotations)
   - [Functions](#functions)
   - [Lists and Dictionaries](#lists-and-dictionaries)
   - [Arrays](#arrays)
4. [Getting Started](#getting-started)
5. [Contributing](#contributing)
6. [Resources](#resources)

---

## **What is Python?**

Python is a high-level, interpreted programming language known for its simplicity and readability. It is widely used in various fields, including web development, data analysis, machine learning, automation, and more.

---

## **How Can Python Be Used?**

Python can be used to:
- Build web applications
- Analyze and visualize data
- Automate repetitive tasks
- Develop machine learning models
- Create games and desktop applications

---

## **Key Concepts Covered**

### Variables
- Declaring variables:
  ```python
  name = "John"
  age = 25
  ```

### Type Annotations
- Adding type hints to variables and functions:
  ```python
  def greet(name: str) -> str:
      return f"Hello, {name}!"
  ```

### Functions
- Declaring and using functions:
  ```python
  def add(a: int, b: int) -> int:
      return a + b
  ```

### Lists and Dictionaries
- Creating and working with lists:
  ```python
  fruits = ["apple", "banana", "cherry"]
  ```
- Defining dictionaries:
  ```python
  person = {"name": "Alice", "age": 30}
  ```

### Arrays
- Arrays using the `array` module or NumPy:
  ```python
  import array
  numbers = array.array('i', [1, 2, 3, 4])
  ```

---

## **Getting Started**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/python-basics-101.git
   ```
2. **Navigate to the directory**:
   ```bash
   cd python-basics-101
   ```
3. **Run the Python examples**:
   ```bash
   python file_name.py
   ```

---

## **Contributing**

Contributions are welcome! If you have suggestions or improvements, feel free to submit a pull request. Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your changes:
   ```bash
   git checkout -b feat/new-feature
   ```
3. Commit and push your changes.
4. Open a pull request.

---

## **Resources**

- [Official Python Documentation](https://docs.python.org/3/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)
- [Python Crash Course](https://nostarch.com/pythoncrashcourse2e)

---

By incorporating this structured README, you make it easier for others (and yourself!) to navigate your repository and understand its purpose. Let me know if you'd like any adjustments!