# import heartrate 
# heartrate.trace(browser=True)

# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))


# if __name__ == "__main__":
#     num = 5
#     print(f"The factorial of {num} is {factorial(num)}")
    # Cool! The bars show the lines that have been hit. The longer bars mean more hits, lighter colors mean more recent.
# From the output above, we can see that the program executes:

# if x==1 5 times
# return 1 once
# return (x * factorial(x-1)) 4 times
# The output makes sense since the initial value of x is 5 and the function is called repetitively until x equals to 1 .

# Now let’s see what it is like to visualize the execution of a Python program in real-time using heartrate. Let’s add sleep(0.5) so that the program runs a little bit slower and increase num to 20 .
import heartrate 
from time import sleep

heartrate.trace(browser=True)


def factorial(x):
    if x == 1:
        return 1
    else:
        sleep(0.5)
        return (x * factorial(x-1))


if __name__ == "__main__":
    num = 20
    print(f"The factorial of {num} is {factorial(num)}")
    # Awesome! We can see which lines of code are being executed and how many times each of them has been executed in real-time.