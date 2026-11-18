# Python Notes

## 1. What is Python?
Python is a high-level, interpreted, general-purpose programming language. It is known for simple and readable syntax.

## 2. Features of Python
- Easy to learn and use
- Interpreted language
- Platform independent
- Object-oriented
- Large standard library
- Supports multiple programming styles

## 3. Installing and Running Python
1. Install Python from https://www.python.org/
2. Open IDLE, a code editor, or a terminal.
3. Save code in a file with the `.py` extension.
4. Run it using `python filename.py`.

## 4. Comments
Comments explain code and are ignored by Python.
```python
# This is a single-line comment
```

## 5. Variables
Variables store values. Python determines the type automatically.
```python
name = "Aqsa"
age = 20
marks = 85.5
```

## 6. Basic Data Types
- `int`: whole numbers, e.g. `10`
- `float`: decimal numbers, e.g. `10.5`
- `str`: text, e.g. `"Hello"`
- `bool`: `True` or `False`
- `list`: ordered, changeable collection
- `tuple`: ordered, unchangeable collection
- `set`: collection of unique values
- `dict`: key-value pairs

## 7. Input and Output
```python
name = input("Enter your name: ")
print("Hello", name)
```
`input()` reads text from the user. Use `int()` or `float()` to convert numeric input.

## 8. Type Conversion
```python
age = int(input("Enter age: "))
price = float("25.50")
text = str(100)
```

## 9. Operators
- Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logical: `and`, `or`, `not`
- Assignment: `=`, `+=`, `-=`, `*=`
- Membership: `in`, `not in`

## 10. Conditional Statements
```python
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

## 11. Loops
### for loop
```python
for i in range(1, 6):
    print(i)
```
### while loop
```python
i = 1
while i <= 5:
    print(i)
    i += 1
```
`break` exits a loop; `continue` skips to the next iteration.

## 12. Strings
Strings are sequences of characters.
```python
word = "Python"
print(word[0])
print(word.upper())
print(word.lower())
print(len(word))
```

## 13. Lists
Lists are ordered and mutable.
```python
numbers = [10, 20, 30]
numbers.append(40)
numbers.remove(20)
print(numbers)
```

## 14. Tuples, Sets, and Dictionaries
```python
point = (2, 3)                 # tuple
unique_numbers = {1, 2, 2, 3} # set
student = {"name": "Aqsa", "age": 20}  # dictionary
print(student["name"])
```

## 15. Functions
A function is a reusable block of code.
```python
def add(a, b):
    return a + b

print(add(5, 3))
```

## 16. Modules
A module is a Python file containing reusable code.
```python
import math
print(math.sqrt(25))
```

## 17. Exception Handling
```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

## 18. Object-Oriented Programming (OOP)
A class is a blueprint; an object is an instance of a class.
```python
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

student = Student("Aqsa")
student.display()
```

## 19. File Handling
```python
with open("example.txt", "w") as file:
    file.write("Hello Python")

with open("example.txt", "r") as file:
    print(file.read())
```

## 20. Useful Built-in Functions
`print()`, `input()`, `len()`, `type()`, `range()`, `sum()`, `min()`, `max()`, `sorted()`

## Practice Tips
- Type and run each example yourself.
- Change input values and observe the output.
- Practise conditions, loops, strings, lists, and functions regularly.
