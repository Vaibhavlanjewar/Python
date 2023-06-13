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
#help(NoneType)

# OOP concepts

# Classes
print("Classes")
#help(class)

# Inheritance
print("Inheritance")
#help(inheritance)

# Polymorphism
print("Polymorphism")
#help(polymorphism)

# Encapsulation
print("Encapsulation")
#help(e#ncapsulation)

# Visualization

# Plot the data types
plt.plot(["Text", "Boolean", "Numeric", "Sequence", "None"], [len(str.__dict__), len(bool.__dict__), len(int.__dict__), len(list.__dict__), len(NoneType.__dict__)])
plt.xlabel("Data type")
plt.ylabel("Number of methods")
plt.title("Number of methods for each data type")
plt.show()
