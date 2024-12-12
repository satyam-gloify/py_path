# print(ord('\t\n\x7E'))
# for char in '\t\n\x7E':
#     print(ord(char))
# 9 10
# print(r'foo\\bar\nbaz')
a=4
# print('adfasdfasdf \t {a}')
# print(r'sfasfasdf  \t {a}')#u, b, br or rb, rf or fr 
# print(f'asdfasd \t {a}') 
# print(rf"The value is {a}\nRaw mode!")  
# a=5
# print(((((13+5)*2)-4)/2)-13 )


# hex_string = "7E"
# bytes_object = bytes.fromhex(hex_string)
# ascii_string = bytes_object.decode("ASCII")
# print(ascii_string)
# print(bytes_object)

# def add(a,b):
#     return a+b

# def subtract(a,b):
#     return a-b

# def printvalu(a):
#     return a

lambda x:x

# if __name__=='__main__':
#     c=add(3,5)
#     print(c)
#     print(printvalu(333))


# print('What is your name')
# name = input()

# print('Hi '+name+', How are you?')

# name=input()

# print('Sounds good..!')

# print('How old r u?')
# age =int(input())

# if(age<18 and age==18):
#     print("Ohh, I didn't know you are younger")
# elif(age>18 and age<30):
#     print('That is great. {age} you knwo I have a question . Are you Married?'.format(age))
# else:
#     print('AAo kbhi haveli pe')


# keywords
#   pass  lambda  except  global  raise exec  nonlocal
#   del complex String(array)
# int an integer can be of any length, memory is the limit

a='red'
del a

# SWAPPING Values
a,b='red','blue'
a,b=b,a
print(a,b)

x=10
printer="Dell"
print("I just printed %s pages to the printer %s" % (x, printer))

# Or you can use the format method.

print("I just printed {0} pages to the printer {1}".format(x, printer))
print("I  just printed {x} pages to the printer {printer}".format(x=7, printer="Dell"))

# A third option is to use f-strings.
print(f"I just printed {x} pages to the printer {printer}")

# Set {} touple () dict {'':''}

# Type Conversion

# You can also use ‘e’ to denote an exponential number.
float("2.1e-2")

# However, this number works even without the float() function.

print(2.1e-2)