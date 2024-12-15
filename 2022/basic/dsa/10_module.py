
# from mymodules import calc # one way to import calc module in current lib

# other way to use exact path - import os
# >>> os.chdir('C:\\Users\\lifei\\Desktop\\calc')
# >>> import calc

from mymodules.submodule import insidecalc as calc

print(calc.add(1,2))
print(calc.mul(5,2))
print(calc.div(7,2))