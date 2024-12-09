# b=8
# def func():
#             a=7
#             print(a)
#             print(b)              
# func()

# //global scop prob
# a=1
# def counter():
#                 a=2
#                 print(a)            
# counter()
# solution
a=1
def counter():
                global a
                a=2
                print(a)    
counter()