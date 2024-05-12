import snoop 

# To understand why the output of factorial(5) is 20 , we can add snoop decorator to the function factorial .
@snoop
def factorial(x: int):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
        
if __name__ == "__main__":
    num = 5
    print(f"The factorial of {num} is {factorial(num)}")