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

# LLLIIISSSTTT = [] , Set ={} ,touple = (), Dictionary = {'':''}

numbers = [1, 2, 3, 4, 5]
squared_numbers = [n**2 for n in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


numbers = [1, 2, 3, 4, 5]
even_squared_numbers = [n**2 for n in numbers if n % 2 == 0]
print(even_squared_numbers)  # Output: [4, 16]

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


# List Comprehension with Nested Loops:

list1 = [1, 2]
list2 = [3, 4]
pairs = [(x, y) for x in list1 for y in list2]
print(pairs)  # Output: [(1, 3), (1, 4), (2, 3), (2, 4)]


# List Comprehension with Multiple Conditions:

filtered_numbers = [n for n in numbers if n % 2 == 0 and n > 3]





######################Set
#Set  is immutable(changable). It does not hold duplicate values

# myset={4,'99'}
# myset.add(55)
# myset.add(5)
# myset.add(25)
# myset.add(445)

# Since a set is unordered, there is no way we can use indexing to access or delete its elements. Then, to perform operations on it,
# Python provides us with a list of functions and methods like discard(), pop(), clear(), remove(), add(), and more. Functions like len() and max() also apply on sets.
# Delete Item from Set 
# myset.discard(8) # If item not found in the set It doesn't generate error 
# myset.remove(3) # If item not found in the set It generate error 
# myset.pop() # Removes the rendom item from the set
# print(myset)
# myset.clear()

myset={1, 2, 3, 4, 5, 6, 3.5}
myset.update([8,9.9])
print(myset)
myset.update([22, 2, 3, 4, 5, 6, 3.5])
print(myset)
len(myset)
min(myset)
max(myset)
sorted(myset)
# sum(myset)

##any
print(any(myset))
##all
# Unlike the any() function, all() returns True only if all items in the Python set have a Boolean value of True. Otherwise, it returns False.
print(all(myset))
print(all({0,'0'}))


###########################python METHODS ON SETS
# So far, we have learned about the methods add(), clear(), discard(), pop(), remove(), and update().
#  Now, we will see more methods from a more mathematical point of view.
# A.UNION
# What it does is it returns all the items that are in any of those sets.
set1,set2,set3={1,2,3},{3,4,5},{5,6,7}
set1.union(set2,set3)

# b. intersection()
# Return common argument in set
set2.intersection(set1)
set2.intersection(set1,set3)

# c. difference()
#  returns the difference of two or more sets.
set1.difference(set2,set3)

# d. symmetric_difference()
# returns all the items that are unique to each set.
set1.symmetric_difference(set2)

# e. intersection_update()
# It stored 3 in set1, because only that was common in set1 and set2
set1.intersection_update(set2)

# f. difference_update()
#  updates the Python set with the difference
set1={1,2,3}
set2={3,4,5}
set1.difference_update(set2)

# g. symmetric_difference_update()
#  it updates the set on which it is called with the symmetric difference.
set1={1,2,3}
set2={3,4,5}
set1.symmetric_difference_update(set2)

# h. copy()
set4=set1.copy()

# i. isdisjoint()
# returns True if two sets have a null intersection.
{1,3,2}.isdisjoint({4,5,6})
# However, it can take only one argument.
# {1,3,2}.isdisjoint({3,4,5},{6,7,8})#can only take 2 arguments

# j. issubset()
# returns true if the set in the argument contains this set.
{1,2}.issubset({1,2,3})
# {1,2} is a proper subset of {1,2,3} and an improper subset of {1,2}.


# k. issuperset()
{1,3,4}.issuperset({1,2})
{1,3,4}.issuperset({1})



###########################7 . python OPERATION ON SETS
'p' in {'a','p','p','l','e'}
'p' not in {'a','p','p','l','e'}
0 not in {'0','1'}

##################################8. Iterating on a Set in Python
for i in {1,3,2}:
    print(i)

#####################9. The frozenset
# A frozen set is in-effect an immutable set.
# frozenset expected at most 1 arguments
#  Also, a set can’t be used a key for a dictionary, but a frozenset can.
# {{1,2}:3}#will release error
#Now lets try with frozenset
# {frozenset(1,2):3}#frozenset expected at most 1 arguments, got 2
{frozenset([1,2]):3}
# 2. Set Comprehensions
# {expression for item in iterable if condition}

a=[[[1,2],[3,4],5],[6,7]]
print(4 in a)



 ######################Touple
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

# Python Tuple Unpacking
colors=('Red','Green','Blue')
a,b,c=colors
print(a,b,c)
# creating a tuple with a single assignment value
a=(1)
print(type(a))
a=(1,)
print(type(a))







##############Dict
# Dictionary Comprehension

# {key_expression: value_expression for item in iterable if condition}


# Example 1: Creating a Dictionary from a List
squared_dict = {n: n**2 for n in numbers} # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Example 2: Creating a Dictionary with a Condition
even_squared_dict = {n: n**2 for n in numbers if n % 2 == 0} # Output: {2: 4, 4: 16, 6: 36}

# Example 3: Inverting a Dictionary
inverted_dict = {v: k for k, v in {'a': 1, 'b': 2, 'c': 3}.items()}
print(inverted_dict)
