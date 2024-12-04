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