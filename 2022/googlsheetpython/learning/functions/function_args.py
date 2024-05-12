# 1. Default Argument in Python
# 2. Python Keyword Arguments


# 3. Python Arbitrary Arguments
def sayhello(*names):
    for name in names:
        print(name)

sayhello('Ayushi','Leo','Megha')
