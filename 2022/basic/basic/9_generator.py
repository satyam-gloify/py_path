## 2 second time and 3 third time
# def simpleGeneratorFun():
#     yield 1            
#     yield 2            
#     yield 3            
   
# # Driver code to check above generat
# print(simpleGeneratorFun())
# for v in simpleGeneratorFun():
#     print(v)



    ##########

# A simple generator for Fibonacci Numbers
def fib(limit):
      
    # Initialize first two Fibonacci Numbers 
    a, b = 0, 1
  
    # One by one yield next Fibonacci Number
    while a < limit: #0<5
        yield a #0
        a, b = b, a + b #a(1)b(1) = 1|,0+1 #a(1),b(1) = 1|, 1 + 1 #a(1),b(2) = 2|, 1+2 #a(2) b(5) = 3|,3+2 

  
# Create a generator object
x = fib(9)
  
# Iterating over the generator object using next
# print(x.next()) # In Python 3, __next__()
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
# for i in fib(5):
#     print(i)