######################Set
#Set  is immutable(changable). It does not hold duplicate values

myset={4,'99'}
# myset.add(55)
# myset.add(5)
# myset.add(25)
# myset.add(445)

# Since a set is unordered, there is no way we can use indexing to access or delete its elements. Then, to perform operations on it, Python provides us with a list of functions and methods like discard(), pop(), clear(), remove(), add(), and more. Functions like len() and max() also apply on sets.
# Delete Item from Set 
# myset.discard(8) # If item not found in the set It doesn't generate error 
# myset.remove(3) # If item not found in the set It generate error 
# myset.pop() # Removes the rendom item from the set
# print(myset)
# myset.clear()

# myset={1, 2, 3, 4, 5, 6, 3.5}
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

