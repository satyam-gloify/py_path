from random import choices, gauss, sample, seed,choice,random, randint, randrange, shuffle

# seed(7)
# print(random())

# with a minimum value 2
# seed(5)
# print(2+10*random())

# Python Random Integers

# seed(4)
# a=randint(0,9), randint(0,9)
# randint(0,9)
# print(a)

# random in range
# print(randrange(-2,10),randrange(-2,10,2))

# seed(7)
# print(gauss(0,1),gauss(0,1),gauss(0,1))

list=[2,4,3,9,6,2,1,0,7,4,3,5,3,6,8]
seed(7)
for i in list:
    print(choice(list))

#For a choice of multiple values 
print(choices(list,k=4))

# Randomly choosing a subset form list

print(sample(list,6))

# Shuffeling a list randomely
print(shuffle(list))