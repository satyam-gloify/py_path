# Aspect    |	Module  |	Package
# Definition    |  Single Python file (.py)	    |   Directory with multiple modules
# Structure	    |   Flat    |	Hierarchical, supports sub-packages
# Usage  |   For small, focused functionality   |	For large-scale organization of modules
# Example   |	math_utils.py   |	utils/ directory with multiple modules



# from mymodules import calc # one way to import calc module in current lib

# other way to use exact path - import os
# >>> os.chdir('C:\\Users\\lifei\\Desktop\\calc')
# >>> import calc

from mypackage.submodule import insidecalc as calc

print(calc.add(1,2))
print(calc.mul(5,2))
print(calc.div(7,2))