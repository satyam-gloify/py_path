"""
With stmt in py is used in exception handling 
to make the code cleaner and much more
readable. 
It simplifies the management of 
common resource like file streams.
"""

####Make the code cleaner with with stmt

# without using with stmt
# 1
file = open('f.ext','w')
file.write('abcd')
file.close()

# 2
file = open('f.ext','w')
try:
    file.write('afd')
finally:
    file.close()


#### using with stmt
with open('file.txt','w') as file:
    file.write('hello !')


# Notice that unlike the first two implementations, there is no need to call file.close() when using with statement. The with statement itself ensures proper acquisition and release of resources. An exception during the file.write() call in the first implementation can prevent the file from closing properly which may introduce several bugs in the code, i.e. many changes in files do not go into effect until the file is properly closed.

### with statement is popularly used with file streams, as shown above and with Locks, sockets, subprocesses and telnets etc.


# To use with statement in user defined objects you only need to add the methods __enter__() and __exit__() in the object methods. Consider the following example for further clarification.


class MyClass(object):
    def  __init__(self,file_Name):
        self.fileName=file_Name
    def __enter__(self):
        self.file =open(self.fileNam,'w')
        return self.file
    def __exit__(self):
        self.file.close()

# 
with MyClass('file.txt') as xfile:
    xfile.write('hello world')

# ###
# Let’s examine the above code. If you notice, what follows the with keyword is the constructor of MessageWriter. As soon as the execution enters the context of the with statement a MessageWriter object is created and python then calls the __enter__() method. In this __enter__() method, initialize the resource you wish to use in the object. This __enter__() method should always return a descriptor of the acquired resource.

#####
# What are resource descriptors?
# handles provided by the operating system to access the
#  requested resources.
file = open('hello.txt')
# in above example the __enter__() method creates a file descriptor
# and return it the name xfile is reference to that discriptor
# #
# In the MessageWriter example provided above, the __enter__() method creates a file descriptor and returns it. The name xfile here is used to refer to the file descriptor returned by the __enter__() method. The block of code which uses the acquired resource is placed inside the block of the with statement. As soon as the code inside the with block is executed, the __exit__() method is called. All the acquired resources are released in the __exit__() method. This is how we use the with statement with user defined objects.

# This interface of __enter__() and __exit__() methods which provides the support of with statement in user defined objects is called Context Manager



from contextlib import contextmanager
  
class MessageWriter(object):
    def __init__(self, filename):
        self.file_name = filename
  
    @contextmanager
    def open_file(self):
        try:
            file = open(self.file_name, 'w')
            yield file
        finally:
            file.close()
  
# usage
message_writer = MessageWriter('hello.txt')
with message_writer.open_file() as my_file:
    my_file.write('hello world')
