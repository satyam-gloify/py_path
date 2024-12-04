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