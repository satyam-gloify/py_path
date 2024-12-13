####################2. Declaring a Boolean
# days=True

# 3. The bool() function
# return true if ther is not empty or null
# >>> bool('Wisdom') return true
# >>> bool([]) returns false


############4. Boolean Values of Various Constructs
# Any empty construct has a Boolean value of False, 
# and a non-empty one has True


# >>> bool(0) return false

# 1 has a Boolean value of True, and so does 0.00000000001.
# >>> bool(0.000000000001) returns true
# >>> bool(' ') return true
# >>> bool('') return false

# 5. Operations on Booleans

# a. Arithmetic
# True+False #1+0 =1
# True+True #1+1=2
# False+False #0+0
# False-True #0-1 = -1
# False/True =0.0 #division resutl is float
# False%True
# False**False
# 0//1
# (True+True)*False+True


###b. Relational
# The relational operators we’ve learnt so far are >, 
# <, >=, <=, !=, and ==. All of these apply to Boolean values.

# c. Bitwise
# Normally, the bitwise operators operate bit-by bit. For example, 
# the following code ORs the bits of 2(010) and 5(101),
#  and produces the result 7(111).

#   OR
#   >>> 2|5 returns 7

#   AND
#   >>> True&False reutrns false

#   XOR - This returns True only if one value is True and one is False.
#   >>> False^True returns true
#   >>> True^True returns true

#   Binary 1’s Complement
#   This calculates 1’s complement for True(1) and False(0).
#   >>> ~True returns -2
#   >>> ~False returns -1

#   Left-shift(<<) and Right-shift(>>) Operators
#   >>> False>>2
#   >>> True<<2

##   d. Identity (is and is not )
#   >>> False is False
#   >>> False is not False

# e. Logical
# >>> False and True returns False








