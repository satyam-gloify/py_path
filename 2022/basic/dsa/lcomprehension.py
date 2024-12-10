# LLLIIISSSTTT = [] , Set ={} ,touple = (), Dictionary = {'':''}

numbers = [1, 2, 3, 4, 5]
squared_numbers = [n**2 for n in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


numbers = [1, 2, 3, 4, 5]
even_squared_numbers = [n**2 for n in numbers if n % 2 == 0]
print(even_squared_numbers)  # Output: [4, 16]

# List Comprehension with Nested Loops:

list1 = [1, 2]
list2 = [3, 4]
pairs = [(x, y) for x in list1 for y in list2]
print(pairs)  # Output: [(1, 3), (1, 4), (2, 3), (2, 4)]


# List Comprehension with Multiple Conditions:

filtered_numbers = [n for n in numbers if n % 2 == 0 and n > 3]

# Python Tuple Unpacking
colors=('Red','Green','Blue')
a,b,c=colors
print(a,b,c)
# creating a tuple with a single assignment value
a=(1)
print(type(a))
a=(1,)
print(type(a))




# Dictionary Comprehension

# {key_expression: value_expression for item in iterable if condition}


# Example 1: Creating a Dictionary from a List
squared_dict = {n: n**2 for n in numbers} # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Example 2: Creating a Dictionary with a Condition
even_squared_dict = {n: n**2 for n in numbers if n % 2 == 0} # Output: {2: 4, 4: 16, 6: 36}

# Example 3: Inverting a Dictionary
inverted_dict = {v: k for k, v in {'a': 1, 'b': 2, 'c': 3}.items()}
print(inverted_dict)


# 2. Set Comprehensions
# {expression for item in iterable if condition}

a=[[[1,2],[3,4],5],[6,7]]
print(4 in a)