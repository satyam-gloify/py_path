
class myfloat:
    def __init__(self,whole,fraction):
        self.whole=whole         
        self.fraction=fraction      
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


