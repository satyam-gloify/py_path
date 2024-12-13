# Comparison
# Aspect  |	Variable |	Namespace
# Definition |	A name referencing a value. |	A container mapping variable names to objects.
# Purpose |	To store and manipulate data. |	To organize variables and avoid naming conflicts.
# Scope |	Can be local or global. |	Encapsulates variables at different levels (local/global).
# Implementation |	References an object directly. |	Acts like a dictionary mapping variable names to objects.
# Example |	x = 5 |	{'x': 5} (part of a namespace)


# rank=1
# Here, ‘rank’ is the name associated with the Python object 1. To get this object’s address in RAM, we use the id() function.
# id(rank) #492979856

x = 10  # 'x' is a variable in the global namespace

def my_func():
    y = 20  # 'y' is a variable in the local namespace of 'my_func'
    print(y)
my_func()

print(globals())  # Prints the global namespace
# Output: {'x': 10, '__name__': '__main__', ...}
def my_func():
    y = 20
    print(locals())  # Prints the local namespace of the function
my_func()
# Output: {'y': 20}

