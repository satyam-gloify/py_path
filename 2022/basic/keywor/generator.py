# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1            
    yield 2            
    yield 3            
   
# Driver code to check above generat
print(simpleGeneratorFun())
for v in simpleGeneratorFun():
    print(v)