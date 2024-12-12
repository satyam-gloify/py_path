
# Python program to illustrate 
# *args for variable number of arguments
def myFun(*argv):
    for arg in argv:
        print (arg)
   
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# Python program to illustrate
# *args with first extra argument
def myFun(arg1, *argv):
    print ("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)
 
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
#########################

# Python program to illustrate 
# *kwargs for variable number of keyword arguments
 
def myFun(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))
 
# Driver code
myFun(first ='Geeks', mid ='for', last='Geeks') 



# Python program to illustrate  **kwargs for
# variable number of keyword arguments with
# one extra argument.
 
def myFun(arg1, **kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))
 
# Driver code
myFun("Hi", first ='Geeks', mid ='for', last='Geeks')  


#################################

def myFun(*args,**kwargs):
	print("args: ", args)
	print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")
