# identity=lambda x:x+1

# print((lambda x:x+1)(6))

# lambda x:x+20

# print(identity)

fullname=lambda a,b,: f'full name: {a.title()}  {b.title()}'

def multply(x1,x2):
    x=x1*x2
    return x
#################### HIGH ORDER LAMBDA FUNCTION ########

A99 = lambda x,add: x+ add

a100=A99(21,multply(10,10))

print(a100)
# print(identity(4))
# print(add(4,5))
# print(fullname('Satyam','Gogal'))


############### Anonymous Functions #################
# The following terms may be used interchangeably depending on the programming language type and culture:

# Anonymous functions
# Lambda functions
# Lambda expressions
# Lambda abstractions
# Lambda form
# Function literals


################################# ARGUMENTS

# Special Symbols Used for passing arguments:-

# 1.)*args (Non-Keyword Arguments)

# 2.)**kwargs (Keyword Arguments)

# >>> (lambda *args: sum(args))(1,2,3)
# 6
# >>> (lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
# 6
# >>> (lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)


########CLOSURE IN PYTHON USING LAMBDA
# def outer_func(x):
#     y = 4
#     return lambda z: x + y + z

# for i in range(3):
#     closure = outer_func(i)
#     print(f"closure({i+5}) = {closure(i+5)}")