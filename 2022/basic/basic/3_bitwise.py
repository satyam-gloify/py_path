# It is typically used in low-level programming for tasks like bit masking, flag setting, or checking specific bits in a binary representation.
# &(and)  |(or) ^(xor) 
# <<(Left Shift) >>(Right Shift) ~(first complement)
# Practical Use Cases
# Permissions Management:
# Example: User roles (read/write/admin) stored as flags.
# Game Development:
# Example: Tracking power-ups (speed boost, shield, etc.).
# System Status:
# Example: Representing which subsystems (disk, network, CPU) are active.
# print(a<<2)


# Let’s take two numbers- 5 and 7. We’ll show you their binary equivalents using the function bin().

# >>> bin(5)
# '0b101' //0b is the prefix to indicate that this is a binary number
# >>> bin(7)
# '0b111'
bin(True) #0b1
bin(False) #0b0
# print(bin(5)[2:])  # Outputs: 101

# diff between and and bitwise & is and returns the first falsey value it encounters or the last value if all are truthy.

print(5 & 7) #bit compirison
print(0&5)
print(12 & 9)  # Output: 8 bit compirison
# diff between and and bitwise & is and returns the first falsey value it encounters or the last value if all are truthy.
# Actually, ‘and’ sees the value on the left. If it has a True Boolean value, it returns whatever value is on the right.

print(-5 & 3)  # Output: 3
# Explanation:
# -5 in binary (two's complement): ...11111011
#  3 in binary:                     ...00000011 011
# Bitwise AND:                      ...00000011 (3 in decimal)


# Masking specific bits
number = 29  # 29 in binary: 11101
mask = 15    # Mask in binary: 01111
print(number & mask)  # Output: 13
# Explanation:
# 29 in binary: 11101
# 15 in binary: 01111
# Bitwise AND: 01101 (13 in decimal)

# Bit Masking: Extract specific bits of a number.
number = 0b101101  # Binary: 45 in decimal
mask = 0b111      # Mask: Extract the last three bits
result = number & mask
print(bin(result))  # Output: 0b101 (Binary for 5)

num = 7
print(num & 1)  # Output: 1 (7 is odd, least significant bit is 1)

num = 8
print(num & 1)  # Output: 0 (8 is even, least significant bit is 0)


# Logical Manipulations with Binary Flags:
FLAG_A = 0b001
FLAG_B = 0b010
FLAG_C = 0b100

# Check if FLAG_B is set / on
current_flags = 0b011  # Both FLAG_A and FLAG_B are set
print(bool(current_flags & FLAG_B))  # Output: True

# Turn FLAG_C ON
current_flags = current_flags | FLAG_C
print(bin(current_flags))  # Output: 0b111
print(bool(current_flags))  # Output: True (FLAG_B is ON)

# Turning a Flag OFF

FLAG_B = 0b010  # 2 in decimal
current_flags = 0b011  # FLAG_A and FLAG_B are ON

# Turn FLAG_B OFF
current_flags = current_flags & ~FLAG_B
print(bin(current_flags))  # Output: 0b001
# current_flags = 0b011 (binary).
# FLAG_B = 0b010 (binary).
# Compute ~FLAG_B (bitwise NOT):
# ~0b010 = 0b101
# Bitwise AND with current_flags:
#   0b011
# & 0b101
# --------
#   0b001  # FLAG_B is OFF, only FLAG_A is ON.

# Toggling a Flag

FLAG_A = 0b001  # 1 in decimal
current_flags = 0b011  # FLAG_A and FLAG_B are ON

# Toggle FLAG_A
current_flags = current_flags ^ FLAG_A
print(bin(current_flags))  # Output: 0b010
# Key Rule:
# The output is 
# 1
# 1 if the inputs are different.
# The output is 
# 0
# 0 if the inputs are the same.



# ~(bitwise first conplement) - This operator takes a number’s binary, and returns its one’s complement.

print(~5)

# print(~1)
#for more can try binary + - * /






#####Thank you so much for such great resource.
# I used to work on embedded project where we used python a lot to manipulate the bits.
# I found, that using bitwise operations, sometimes you code could be mode compact even though for me it takes some time to understand. Let say i can convert the bits to string then change the way i want then convert back (this simple example) which is not optimal.
# I am wondering is there any set of standardized shortcuts (bitwise tricks, bitwise coockbook) that developers are using, that i can learn and used in future or it comes with experience?
# I am sorry cannot give you exact example of code.
# Thanks in advance

