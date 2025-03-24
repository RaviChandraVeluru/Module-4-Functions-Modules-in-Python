#Calculate Factorial using a function
#1. define a function named factorial that takes a number as an argument and calculates its factorial using a loop or
#recursion.
#2. Returns the calculated Factorial.
#3. Calls the function with a sample number and prints the output

def factorial(num):
    factorial = 1
    i = 2
    while i <= num:
        factorial *=i
        i+=1
    return factorial
user_input = int(input("Enter a number that you want to find out Factorial: "))
result = factorial(user_input)
print("factorial of " + str (user_input) +" is", result )