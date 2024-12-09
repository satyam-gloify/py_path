from random import choices, gauss, sample, seed,choice,random, randint, randrange, shuffle
from numpy.random import seed, rand

# seed(7)
# print(random())
# Python Seed() is used to initialize the random number generator. The random number generator needs a number to start with (a seed value), to be able to generate a random number.
# If you are not using the seed(n), then it will take time as seed value. seed(n) help us in generating the same value again and again.
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


# Generate Python Random Number with NumPy?
# from numpy.random import seed
# >>> from numpy.random import rand
print(seed(7))
print(rand(3))