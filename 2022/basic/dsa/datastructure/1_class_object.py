# Python provides several special methods that define the behavior of classes and their instances at various stages:
# __new__: Responsible for creating a new instance (called before __init__).
# __init__: Initializes the instance.
# __del__: Cleans up resources when the object is destroyed.
# __repr__, __str__: Define how the object is represented as a string.

class myfloat:
    def __new__(cls, *args, **kwargs):
        print("Creating an instance")
        return super().__new__(cls)
    def __init__(self,whole,fraction):
        self.whole=whole         
        self.fraction=fraction     
        
    def __del__(self):
        # Called when an object is garbage collected.
        print("Object is being destroyed.") 
    def shownumber(self):       
                print(f"I am {self.whole}.{self.fraction}")
    #without add function pg will give error
    def __add__(self,other):      
        if (self.fraction+other.fraction)>9:                                        
            return myfloat(self.whole+other.whole+1,self.fraction+other.fraction-10)
        return myfloat(self.whole+other.whole,self.fraction+other.fraction)
obj1=myfloat(3,7)
obj1.shownumber()

obj2=myfloat(3,3)
obj2.shownumber()

obj1+obj2


class itspower:                
        def __init__(self,x):                  
               self.x=x                
        def __pow__(self,other):                               
               return self.x**other.x             
a=itspower(2)
b=itspower(10)
print(a**b)


#################

#  a simple file writer object
  
  
class MessageWriter(object):
    def __init__(self, file_name):
        self.file_name = file_name
      
    def __enter__(self):
        self.file = open(self.file_name, 'w')
        return self.file
  
    def __exit__(self, exc_type, exc_value, traceback):
#   Part of the context management protocol.
#   Explicitly called when exiting a with block.
#   Ensures predictable cleanup.
        self.file.close()
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return False  # Propagate exceptions
  
# using with statement with MessageWriter
  
with MessageWriter('my_file.txt') as xfile:
    xfile.write('hello world')
file = open('hello.txt')


# How __enter__ and __exit__ Work Together
# Classes implementing __enter__ and __exit__ are called context managers.
# The with statement ensures that:
# __enter__: is executed before the block starts.
# __exit__: is executed when the block ends, even if an exception is raised.
# __call__: Enables an instance to be called like a function.

class SuppressErrors:
    def __enter__(self):
        print("Entering block")
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting block")
        return True  # Suppress all exceptions

with SuppressErrors():
    raise ValueError("This error is suppressed!")
print("Execution continues.")