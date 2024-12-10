 ######################List
#Touple is not is immutable(unchangable changable)
colors=('Red','Green','Blue',4,6.6)
a=1,
print(type(a))

#  Python Tuple Packing
mytuple=1,2,3,       #Or it could have been mytuple=1,2,3

print(mytuple[1])
# Python Tuple Unpacking
a,b,c=mytuple
print(a,b,c)
# TypeError: ‘tuple’ object does not support item deletion
del mytuple[1]
# instead del mytuple
########Touple Operations
#same as list 