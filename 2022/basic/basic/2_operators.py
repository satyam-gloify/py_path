# Precedence of Arithmetic Operators in Python

# The precedence of Arithmetic Operators in Python is as follows:

# P – Parentheses
# E – Exponentiation
# M – Multiplication (Multiplication and division have the same precedence)
# D – Division
# A – Addition (Addition and subtraction have the same precedence)
# S – Subtraction

# import operator

# # Test values for comparison
# a = 10
# b = 20
# c = 10
# d = "apple"
# e = "banana"

# # Using the preferred operator functions (without double underscores)
# print("Using operator functions:")
# print(f"a < b: {operator.lt(a, b)}")   # a < b (10 < 20)
# print(f"a <= b: {operator.le(a, b)}")  # a <= b (10 <= 20)
# print(f"a == c: {operator.eq(a, c)}")  # a == c (10 == 10)
# print(f"a != b: {operator.ne(a, b)}")  # a != b (10 != 20)
# print(f"a >= b: {operator.ge(a, b)}")  # a >= b (10 >= 20)
# print(f"a > b: {operator.gt(a, b)}")   # a > b (10 > 20)

# # Testing with strings
# print(f"d < e: {operator.lt(d, e)}")   # d < e ("apple" < "banana")

# # Using the special methods (with double underscores)
# print("\nUsing special methods (with double underscores):")
# print(f"a < b: {operator.__lt__(a, b)}")   # a < b (10 < 20)
# print(f"a <= b: {operator.__le__(a, b)}")  # a <= b (10 <= 20)
# print(f"a == c: {operator.__eq__(a, c)}")  # a == c (10 == 10)
# print(f"a != b: {operator.__ne__(a, b)}")  # a != b (10 != 20)
# print(f"a >= b: {operator.__ge__(a, b)}")  # a >= b (10 >= 20)
# print(f"a > b: {operator.__gt__(a, b)}")   # a > b (10 > 20)

# # You can also compare strings using special methods
# print(f"d < e: {operator.__lt__(d, e)}")   # d < e ("apple" < "banana")


#floor(int) division and float divident
print(10//2)
print(10/2)

# diff between and and bitwise & is and returns the first falsey value it encounters or the last value if all are truthy.
# Actually, ‘and’ sees the value on the left. If it has a True Boolean value, it returns whatever value is on the right.

print(True and True)   # Output: True (Both are truthy, so it evaluates to the second value, which is True)
print(True and False)  # Output: False (The second value is falsey, so it returns False)
print(False and True)  # Output: False (The first value is falsey, so it stops there)
print(False and False) # Output: False (The first value is falsey, so it stops there)
print(5.3 and 4) 
print(5 and 4)    # Output: 4 (5 is truthy, so it evaluates and returns 4)
print(0 and 4)    # Output: 0 (0 is falsey, so the evaluation stops at 0)
print(4 and 0)    # Output: 0 (4 is truthy, but 0 is falsey)
print(0 and 0)
print("Hello" and "World")   # Output: "World" (Both are truthy, so it returns the second value)
print("" and "World")        # Output: "" (The first value is falsey, so it stops there)
print("Hello" and "")        # Output: "" (The first value is truthy, so it evaluates and returns the second)
print("" and "") 


# Operators Overloading for all operators
# What Is Operator Overloading?
# Normally, operators work for predefined data types. For example:
# +	__add__(self, other)	Addition
# -	__sub__(self, other)	Subtraction
# *	__mul__(self, other)	Multiplication
# /	__truediv__(self, other)	Division
# %	__mod__(self, other)	Modulus
# **	__pow__(self, other)	Power
# ==	__eq__(self, other)	Equality
# !=	__ne__(self, other)	Not equal
# >	__gt__(self, other)	Greater than
# <	__lt__(self, other)	Less than
# >=	__ge__(self, other)	Greater than or equal to
# <=	__le__(self, other)	Less than or equal to
# []	__getitem__(self, key)	Indexing
# Advance
# __str__: Defines the string representation for an object.
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name}"

p = Person("Alice")
print(p)  # Output: My name is Alice

# Object Representation
# __repr__: Used for debugging. Should return an unambiguous string.
def __repr__(self):
    return f"Person({self.name})"

# Length
# __len__: Used to define the behavior of len().
class CustomList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

cl = CustomList([1, 2, 3])
print(len(cl))  # Output: 3

# Item Access
# __getitem__: For indexing.
# __setitem__: For assigning values to indices.
# # Addition for numbers
# print(3 + 4)  # Output: 7

# # Concatenation for strings
# print("Hello" + " World")  # Output: Hello World
# When you create your own classes, operators like + or - won’t work on objects of those classes unless you overload them using magic methods.

# How to Overload Operators in Python
# Step 1: Use Magic Methods

# Magic methods start and end with __ (double underscores). Each operator has a corresponding magic method. For example:

# +: __add__
# -: __sub__
# *: __mul__
# /: __truediv__

# Example 1: Overloading +

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Overload `+` to add two Point objects
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Test the class
p1 = Point(1, 2)
p2 = Point(3, 4)
result = p1 + p2  # This calls p1.__add__(p2)
print(result)  # Output: Point(4, 6)



# Overloading Comparison Operators (>, <, ==)

class Box:
    def __init__(self, volume):
        self.volume = volume

    def __gt__(self, other):
        # Overload `>` to compare volumes
        return self.volume > other.volume

    def __eq__(self, other):
        # Overload `==` to check equality of volumes
        return self.volume == other.volume

# Test the class
box1 = Box(100)
box2 = Box(150)
print(box1 > box2)  # Output: False
print(box1 == box2)  # Output: False