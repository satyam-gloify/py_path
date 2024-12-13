# a=3
# while(a>0):
#         print(a)
#         a-=1
# else:
#     print("Reached 0")
############## OR
# a=3
# while(a>0):
#         print(a)
#         a-=1
#         if a==1: break
# else:
#     print("Reached 0")


########## single line stmt
# while a>0: print(a); a-=1

# ########### 
# print(list(range(10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(range(2,7)))#[2, 3, 4, 5, 6]
# # You can also pass three arguments. The third argument is the interval.
# print(list(range(2,12,2)))#[2, 4, 6, 8, 10]
# print(list(range(12,2,-2)))#[12, 10, 8, 6, 4]
# print(list(range(12,2,2)))#Will return []
# print(list(range(12,2))) #Will return []
# print(list(range(2,12,-2))) #Will return []

#####if else for loop
#for i in range(10):
#      print(i)
#else:
#      print("Reached else")

###Continue Stmt
# i=0
# while(i<8):
#         i+=1
#         if(i==6): continue
#         print(i)

# ###3. pass statement
#       In Python, we use the pass statement to implement stubs.
#       When we need a particular loop, class, or function in our 
#       program, but don’t know what goes in it,
#        we place the pass statement in it.

#       It is a null statement.
#       The interpreter does not ignore it, but it performs a no-operation (NOP).
for i in 'selfhelp':
    pass

print(i)
