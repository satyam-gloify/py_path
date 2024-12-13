##########CLOSURE
# A closure is a function where every free variable, everything except parameters, used in that function is bound to a specific value defined in the enclosing scope of that function. In effect, closures define the environment in which they run, and so can be called from anywhere.

# Here’s a closure constructed with a normal Python function:

def outer_func(x):
    y = 4
    def inner_func(z):
        print(f"x = {x}, y = {y}, z = {z}")
        return x + y + z
    return inner_func

for i in range(3):
    closure = outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")
# outer_func() returns inner_func(), a nested function that computes the sum of three arguments:

# x is passed as an argument to outer_func().
# y is a variable local to outer_func().
# z is an argument passed to inner_func().
# To test the behavior of outer_func() and inner_func(), outer_func() is invoked three times in a for loop that prints the following:

# x = 0, y = 4, z = 5
# closure(5) = 9
# x = 1, y = 4, z = 6
# closure(6) = 11
# x = 2, y = 4, z = 7
# closure(7) = 13