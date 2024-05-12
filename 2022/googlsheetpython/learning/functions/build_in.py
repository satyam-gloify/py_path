# 1. abs()
# absolute value

# 2. all()=> >>> all([' ',' ',' '])
#  returns True if all values in a iterable have a Boolean value of True.

# 3. any() +. >>> any((1,0,0))
# returns True if, even one value in the iterable has a Boolean value of True.

# 4.  ascii()
# returns a printable representation of a python object (like a string or a Python list).
# >>> ascii('ș')
# output=>
# Since this was a non-ASCII character in python, the interpreter added a backslash (\) and escaped it using another backslash.
# >>> ascii('ușor')
# output=>
# Let’s apply it to a list.
# >>> ascii(['s','ș'])

# 5. bin()
# convert int to bin

# 6. bool()

# 7. bytearray() #mutable
# bytearray() returns a python array of a given byte size.
# >>> a=bytearray(4)
# output =>bytearray(b’\x00\x00\x00\x00′)
# >>> a.append(1)
# bytearray(b’\x00\x00\x00\x00\x01′)
# >>> a[0]=1
# >>> a[0]=1
# >>> a

# 8. bytes() #immutable
# bytes() returns an immutable bytes object.
# >>> bytes([1,2,3,4,5])
# >>> bytes('hello','utf-8')
# Both bytes() and bytearray() deal with raw data, but bytearray() is mutable, while bytes() is immutable.
# >>> a=bytes([1,2,3,4,5])
# >>> a[4]= //error 

# 9. callable()
# callable() tells us if an object can be called.
# >>> callable([1,2,3]) # False
# >>> callable(callable) # True
# >>> callable(False) #False
# >>> callable(list) #True

# 10. chr(ASCIIVALUEINt)
# ascii -> char
# >>> chr(97) #'a'

# 11. classmethod()
# returns a class method for a given method.
# >>> class fruit:
#                 def sayhi(self):
#                                 print("Hi, I'm a fruit") 
       
# >>> fruit.sayhi=classmethod(fruit.sayhi)
# >>> fruit.sayhi()

# 12. compile()
# string code -> object code
# >>> exec(compile('a=5\nb=7\nprint(a+b)','','exec'))
# output => 12

# 13. complex()
# # convert no to  complex no
# >>> complex(3+5j)
# >>> complex(3.5j)

# 14. delattr()# delete attribute like data member in class
# >>> class fruit:
#                 size=7  
         
# >>> orange=fruit()
# >>> orange.size
# >>> delattr(fruit,'size')
# >>> orange.size #output 7
# >>> delattr(fruit,'size')
# >>> orange.size #AttributeError: ‘fruit’ object has no attribute ‘size’

# 15. dict()
# dict(), as we have seen it, creates a python dictionary.
# >>> dict()

# 16. dir()
# dir() returns an object’s attributes.

# >>> class fruit:
#                 size=7
#                 shape='round'
# >>> orange=fruit()
# >>> dir(orange)

# 17. divmod()
# it returns the floor division and the modulus of the two numbers.
# >>> divmod(3,7) #(0,3)
# >>> divmod(7,3) #(2,1)

# 18. enumerate()
# # This Python Built In function returns an enumerate object. In other words, it adds a counter to the iterable.
# >>> for i in enumerate(['a','b','c']):
#                 print(i)

# 19. eval()
# >>> x=7
# >>> eval('x+7') output 14

# 20. exec()
# exec() runs Python code dynamically.
# >>> exec('a=2;b=3;print(a+b)') output 5

# 21. filter()
# Like we’ve seen in python Lambda Expressios, filter() filters out the items for which the condition is True.
# >>> list(filter(lambda x:x%2==0,[1,2,0,False]))

# We have seen this Python built-in function, one in our lesson on Python Strings.
# 23. format()
# >>> a,b=2,3
# >>> print("a={0} and b={1}".format(a,b))
# >>> print("a={a} and b={b}".format(a=3,b=4))

# 25.getattr()
# returns the value of an object’s attribute.
# >>> getattr(orange,'size') output 7

# 26. globals()
# returns a dictionary of the current global symbol table.
# >>> globals()

# 27. hasattr()
# Like delattr() and getattr(), hasattr() Python built-in functions, returns True if the object has that attribute.