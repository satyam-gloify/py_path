mylist=[]
for i in 'anxiety':
   mylist.append(i)
print(mylist)

###########################
# print( [i for i in 'anxiety'])

###################
# print([i*2 for i in {3,1,2}])


#######################Python List Comprehension vs Lambda Expression
myset={3,1,2}
makelist=lambda i:list(i)
mylist=makelist(myset)
# print(mylist)

# To do this using the map function instead, we write the following code:
a=list(map(lambda i:i,myset))
print(a)

######Conditionals in Python List Comprehension
    #Single Condition
    # >>> [i for i in range(8) if i%2!=0]

    #Nested condition
    # >>> [i for i in range(8) if i%2==0 if i%3==0]
    # output [0, 6]

    # b. if..else in List Comprehension in Python
    # >>> ["Even" if i%2==0 else "Odd" for i in range(8)]

# ###########Nested List Comprehension in Python
# simple way 
# print table for 7 and  8
# >>> for i in range(7,9):
#         for j in range(1,11):
#                print(f"{i}*{j}={i*j}")

# Compresension way
# >>> [[i*j for j in range(1,11)] for i in range(7,9)]
