######################List
#List  is immutable(changable)
# myList=[1,2,False,'No',3.3]

# myList.remove("No")
# print(type(myList[3]))
# myList[start,n-1]
# print(myList[0:4])
# print(myList)
list1=[1,[2,3],(4,5),False,'No',33,33,21,21,345,]

print(list1)
# print(list1[:-3])
# del list1[1]
# list1.remove(21)
del list1[3:-1]
print(list1)
list1[1:3]=[9,10,11]
print(list1)