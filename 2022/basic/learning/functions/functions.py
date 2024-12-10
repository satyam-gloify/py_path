# doc string
def hello():
    """
    This Python function simply prints hello to the screen
    """
    print("Hello")
# You can access this docstring using the __doc__ 
# attribute of the function.

print(hello.__doc__)

###############h. Deleting Python function
#   >>> def func7():
#           print("7")
#   >>> func7()
    
#   #Delete
#   >>> del func7
#   >>> func7()


#######Recursive function
# >>> def facto(n):
#   if n==1:
#     return 1
#   return n*facto(n-1)
# >>> facto(5)