# -*- coding: utf-8 -*-
"""Python_Cheat_sheat.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ie7A5-v1b3eIJVxN0jCNN5oaJKDB4P8A
"""

import matplotlib.pyplot as plt

# Data types

# Text type
print("Text type")
help(str)

# Boolean type
print("Boolean type")
help(bool)

# Numeric types
print("Numeric types")
help(int)
help(float)
help(complex)

# Sequence types
print("Sequence types")
help(list)
help(tuple)
help(range)

# None type


# OOP concepts

# Classes
print("Classes")

class apple:

   colour=""
   flavour=""
a=apple()
a.colour="Red"
a.flavour="Sweet"
print(a.colour)
print(a.flavour)
help(apple)



# Visualization

# Plot the data types
plt.plot(["Text", "Boolean", "Numeric", "Sequence", "None"], [len(str.__dict__), len(bool.__dict__), len(int.__dict__), len(list.__dict__), len(NoneType.__dict__)])
plt.xlabel("Data type")
plt.ylabel("Number of methods")
plt.title("Number of methods for each data type")
plt.show()

import matplotlib.pyplot as plt

# Numeric Data Types
x = 5  # Integer
y = 3.14  # Float
z = 2 + 3j  # Complex

# Sequence Data Types
string = "Hello, World!"  # String
my_list = [1, 2, 3, 4, 5]  # List
my_tuple = (1, 2, 3, 4, 5)  # Tuple

# Mapping Data Types
my_dict = {'name': 'John', 'age': 30}  # Dictionary

# Set Data Types
my_set = {1, 2, 3, 4, 5}  # Set
my_frozenset = frozenset({1, 2, 3, 4, 5})  # Frozen Set

# Conditional Statements
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x and y are equal")

# Looping Statements
for i in range(5):
    print(i)

while x > 0:
    print(x)
    x -= 1

# Defining Functions
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(f"The result of adding numbers is: {result}")

# Lambda Functions
multiply = lambda a, b: a * b
result = multiply(5, 3)
print(f"The result of multiplying numbers is: {result}")

# Object-Oriented Programming (OOP)
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

my_rectangle = Rectangle(5, 3)
print(f"The area of the rectangle is: {my_rectangle.area()}")
print(f"The perimeter of the rectangle is: {my_rectangle.perimeter()}")

# Standard Input/Output
name = input("Enter your name: ")
print(f"Hello, {name}!")

print("Hello, World!")

# File Input/Output
filename = "myfile.txt"
with open(filename, "a+") as file:
    file.seek(0)  # Move the file cursor to the beginning
    if file.read() == "":
        file.write("Sample content")

with open(filename, "r") as file:
    content = file.read()
    print(content)

# Data Visualization
data = [1, 2, 3, 4, 5]
plt.plot(data)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Data Visualization')
plt.show()

# Writing the code to a Python file
code = '''
{}
'''

filename = "python_cheat_sheet.py"
with open(filename, "w") as file:
    file.write(code.format(code))

print(f"Python cheat sheet code has been written to {filename} successfully!")

import matplotlib.pyplot as plt

# Data types

# Text type
print("Text type")
help(str)

# Boolean type
print("Boolean type")
help(bool)

# Numeric types
print("Numeric types")
help(int)
help(float)
help(complex)

# Sequence types
print("Sequence types")
help(list)
help(tuple)
help(range)

# None type
print("None type")
help(type(None))

# OOP concepts

# Classes
print("Classes")
help(type)

# Inheritance
print("Inheritance")
help(type.mro)

# Polymorphism
print("Polymorphism")
help(type)

# Encapsulation
print("Encapsulation")
help(type)

# Visualization

# Plot the data types
data_types = ["Text", "Boolean", "Numeric", "Sequence", "None"]
num_methods = [len(str.__dict__), len(bool.__dict__), len(int.__dict__), len(list.__dict__), len(type(None).__dict__)]

plt.plot(data_types, num_methods)
plt.xlabel("Data type")
plt.ylabel("Number of methods")
plt.title("Number of methods for each data type")
plt.show()

# Writing the code to a Python file
code = """
import matplotlib.pyplot as plt

# Data types

# Text type
print("Text type")
help(str)

# Boolean type
print("Boolean type")
help(bool)

# Numeric types
print("Numeric types")
help(int)
help(float)
help(complex)

# Sequence types
print("Sequence types")
help(list)
help(tuple)
help(range)

# None type
print("None type")
help(type(None))

# OOP concepts

# Classes
print("Classes")
help(type)

# Inheritance
print("Inheritance")
help(type.mro)

# Polymorphism
print("Polymorphism")
help(type)

# Encapsulation
print("Encapsulation")
help(type)

# Visualization

# Plot the data types
data_types = ["Text", "Boolean", "Numeric", "Sequence", "None"]
num_methods = [len(str.__dict__), len(bool.__dict__), len(int.__dict__), len(list.__dict__), len(type(None).__dict__)]

plt.plot(data_types, num_methods)
plt.xlabel("Data type")
plt.ylabel("Number of methods")
plt.title("Number of methods for each data type")
plt.show()
"""

filename = "python_cheat_sheet.py"
with open(filename, "w") as file:
    file.write(code)

print(f"Python cheat sheet code has been written to {filename} successfully!")

import matplotlib.pyplot as plt
import random

# Data types

# Text type
print("Text type")
help(str)

# Boolean type
print("Boolean type")
help(bool)

# Numeric types
print("Numeric types")
help(int)
help(float)
help(complex)

# Sequence types
print("Sequence types")
help(list)
help(tuple)
help(range)

# Set type
print("Set type")
help(set)
help(frozenset)

# Mapping type
print("Mapping type")
help(dict)

# None type
print("None type")
help(type(None))

# OOP concepts

# Classes
class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")

print("Class")
help(MyClass)

# Inheritance
class MyChildClass(MyClass):
    def __init__(self, value):
        super().__init__(value)

print("Inheritance")
help(MyChildClass)

# Polymorphism
def polymorphic_function(obj):
    obj.display()

print("Polymorphism")
help(polymorphic_function)

# Encapsulation
class MyEncapsulationClass:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def set_value(self, new_value):
        self.__value = new_value

print("Encapsulation")
help(MyEncapsulationClass)

# Random module
print("Random module")
help(random)

# List comprehension
print("List comprehension")
help(list.append)
help(list.extend)
help(list.insert)
help(list.remove)
help(list.pop)
help(list.index)
help(list.count)
help(list.sort)
help(list.reverse)

# Data structures
print("Data structures")

# List
print("List")
help(list)

# Tuple
print("Tuple")
help(tuple)

# Set
print("Set")
help(set)

# Dictionary
print("Dictionary")
help(dict)

# Visualization

# Plot the data types
data_types = ["Text", "Boolean", "Numeric", "Sequence", "Set", "Mapping", "None"]
num_methods = [
    len(str.__dict__), len(bool.__dict__), len(int.__dict__), len(list.__dict__),
    len(set.__dict__), len(dict.__dict__), len(type(None).__dict__)
]

plt.bar(data_types, num_methods)
plt.xlabel("Data type")
plt.ylabel("Number of methods")
plt.title("Number of methods for each data type")
plt.show()

# Writing the code to a Python file
code = """
import matplotlib.pyplot as plt
import random

# Data types

# Text type
print("Text type")
help(str)

# Boolean type
print("Boolean type")
help(bool)

# Numeric types
print("Numeric types")
help(int)
help(float)
help(complex)

# Sequence types
print("Sequence types")
help(list)
help(tuple)
help(range)

# Set type
print("Set type")
help(set)
help(frozenset)

# Mapping type
print("Mapping type")
help(dict)

# None type
print("None type")
help(type(None))

# OOP concepts

# Classes
class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")

print("Class")
help(MyClass)

# Inheritance
class MyChildClass(MyClass):
    def __init__(self, value):
        super().__init__(value)

print("Inheritance")
help(MyChildClass)

# Polymorphism
def polymorphic_function(obj):
    obj.display()

print("Polymorphism")
help(polymorphic_function)

# Encapsulation
class MyEncapsulationClass:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def set_value(self, new_value):
        self.__value = new_value

print("Encapsulation")
help(MyEncapsulationClass)

# Random module
print("Random module")
help(random)

# List comprehension
print("List comprehension")
help(list.append)
help(list.extend)
help(list.insert)
help(list.remove)
help(list.pop)
help(list.index)
help(list.count)
help(list.sort)
help(list.reverse)

# Data structures
print("Data structures")

# List
print("List")
help(list)

# Tuple
print("Tuple")
help(tuple)

# Set
print("Set")
help(set)

# Dictionary
print("Dictionary")
help(dict)

# Visualization

# Plot the data types
data_types = ["Text", "Boolean", "Numeric", "Sequence", "Set", "Mapping", "None"]
num_methods = [
    len(str.__dict__), len(bool.__dict__), len(int.__dict__), len(list.__dict__),
    len(set.__dict__), len(dict.__dict__), len(type(None).__dict__)
]

plt.bar(data_types, num_methods)
plt.xlabel("Data type")
plt.ylabel("Number of methods")
plt.title("Number of methods for each data type")
plt.show()
"""

filename = "python_cheat_sheet.py"
with open(filename, "w") as file:
    file.write(code)

print(f"Python cheat sheet code has been written to {filename} successfully!")

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Data types

# Text type
print("Text type")
help(str)

# Boolean type
print("Boolean type")
help(bool)

# Numeric types
print("Numeric types")
help(int)
help(float)
help(complex)

# Sequence types
print("Sequence types")
help(list)
help(tuple)
help(range)

# Set type
print("Set type")
help(set)
help(frozenset)

# Mapping type
print("Mapping type")
help(dict)

# None type
print("None type")
help(type(None))

# OOP concepts

# Classes
class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")

print("Class")
help(MyClass)

# Inheritance
class MyChildClass(MyClass):
    def __init__(self, value):
        super().__init__(value)

print("Inheritance")
help(MyChildClass)

# Polymorphism
def polymorphic_function(obj):
    obj.display()

print("Polymorphism")
help(polymorphic_function)

# Encapsulation
class MyEncapsulationClass:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def set_value(self, new_value):
        self.__value = new_value

print("Encapsulation")
help(MyEncapsulationClass)

# Random module
print("Random module")
help(random)

# List comprehension
print("List comprehension")
help(list.append)
help(list.extend)
help(list.insert)
help(list.remove)
help(list.pop)
help(list.index)
help(list.count)
help(list.sort)
help(list.reverse)

# Data structures
print("Data structures")

# List
print("List")
help(list)

# Tuple
print("Tuple")
help(tuple)

# Set
print("Set")
help(set)

# Dictionary
print("Dictionary")
help(dict)

# Visualization

data_types = ["Text", "Boolean", "Numeric", "Sequence", "Set", "Mapping", "None"]
num_methods = [
    len(str.__dict__), len(bool.__dict__), len(int.__dict__), len(list.__dict__),
    len(set.__dict__), len(dict.__dict__), len(type(None).__dict__)
]

fig, ax = plt.subplots()

ax.bar(data_types, num_methods)
ax.set_xlabel("Data type")
ax.set_ylabel("Number of methods")
ax.set_title("Number of methods for each data type")

def animate(i):
    random.shuffle(num_methods)
    ax.clear()
    ax.bar(data_types, num_methods)
    ax.set_xlabel("Data type")
    ax.set_ylabel("Number of methods")
    ax.set_title("Number of methods for each data type (Animation)")

ani = animation.FuncAnimation(fig, animate, frames=10, interval=1000, repeat=True)

plt.show()

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Function to print colored text
def print_colored_text(text, color):
    colors = {
        "red": "\u001b[31m",
        "green": "\u001b[32m",
        "yellow": "\u001b[33m",
        "blue": "\u001b[34m",
        "reset": "\u001b[0m"
    }
    color_code = colors.get(color.lower())
    if color_code:
        print(f"{color_code}{text}{colors['reset']}")
    else:
        print(text)

# Data types

# Text type
print_colored_text("Text type", "blue")
help(str)

# Boolean type
print_colored_text("Boolean type", "blue")
help(bool)

# Numeric types
print_colored_text("Numeric types", "blue")
help(int)
help(float)
help(complex)

# Sequence types
print_colored_text("Sequence types", "blue")
help(list)
help(tuple)
help(range)

# Set type
print_colored_text("Set type", "blue")
help(set)
help(frozenset)

# Mapping type
print_colored_text("Mapping type", "blue")
help(dict)

# None type
print_colored_text("None type", "blue")
help(type(None))

# OOP concepts

# Classes
print_colored_text("Classes", "blue")
class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")

help(MyClass)

# Inheritance
print_colored_text("Inheritance", "blue")
class MyChildClass(MyClass):
    def __init__(self, value):
        super().__init__(value)

help(MyChildClass)

# Polymorphism
print_colored_text("Polymorphism", "blue")
def polymorphic_function(obj):
    obj.display()

help(polymorphic_function)

# Encapsulation
print_colored_text("Encapsulation", "blue")
class MyEncapsulationClass:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def set_value(self, new_value):
        self.__value = new_value

help(MyEncapsulationClass)

# Random module
print_colored_text("Random module", "blue")
help(random)

# List comprehension
print_colored_text("List comprehension", "blue")
help(list.append)
help(list.extend)
help(list.insert)
help(list.remove)
help(list.pop)
help(list.index)
help(list.count)
help(list.sort)
help(list.reverse)

# Data structures
print_colored_text("Data structures", "blue")

# List
print_colored_text("List", "blue")
help(list)

# Tuple
print_colored_text("Tuple", "blue")
help(tuple)

# Set
print_colored_text("Set", "blue")
help(set)

# Dictionary
print_colored_text("Dictionary", "blue")
help(dict)

# Visualization

data_types = ["Text", "Boolean", "Numeric", "Sequence", "Set", "Mapping", "None"]
num_methods = [
    len(str.__dict__), len(bool.__dict__), len(int.__dict__), len(list.__dict__),
    len(set.__dict__), len(dict.__dict__), len(type(None).__dict__)
]

fig, ax = plt.subplots()

ax.bar(data_types, num_methods)
ax.set_xlabel("Data type")
ax.set_ylabel("Number of methods")
ax.set_title("Number of methods for each data type")

def animate(i):
    random.shuffle(num_methods)
    ax.clear()
    ax.bar(data_types, num_methods)
    ax.set_xlabel("Data type")
    ax.set_ylabel("Number of methods")
    ax.set_title("Number of methods for each data type (Animation)")

ani = animation.FuncAnimation(fig, animate, frames=10, interval=1000, repeat=True)

plt.show()