# # <value_if_true> if <condition> else <value_if_false>



# # Comparison with Traditional if-else
# # Here’s a comparison of the ternary operator and a traditional if-else block:

# # Using if-else Block:

# x = 5
# y = 10

# if x < y:
#     min_value = x
# else:
#     min_value = y
# print(min_value)  # Output: 5

# # Using Ternary Operator:
# min_value = x if x < y else y
# print(min_value)  # Output: 5


# a, b, c = 5, 10, 15

# # Nested ternary
# result = "A is largest" if a > b and a > c else ("B is largest" if b > c else "C is largest")
# print(result)  # Output: C is largest

def zero():
        return 'zero'
def one():
        return 'one'
def indirect(i):
    switcher={
            0:zero,
            1:one,
            2:lambda:'two'
            }
    func=switcher.get(i,lambda :'Invalid')
    return func()

def indirect(i):
       switcher={
              0:zero,
              1:one,
       }
       func=switcher.get(i,"Invalid day of week")

print(indirect(3))


# With Python Classes

# Using this concept with classes lets us choose a method at runtime.
class Switcher(object):
          def indirect(self,i):
                   method_name='number_'+str(i)
                   method=getattr(self,method_name,lambda :'Invalid')
                   return method()
          def number_0(self):
                   return 'zero'
          def number_1(self):
                   return 'one'
          def number_2(self):
                   return 'two'
s=Switcher()
s.indirect(2)