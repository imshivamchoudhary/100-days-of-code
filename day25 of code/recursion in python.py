# recursion in python
# recursion is the process of defining something in terms of itself

# python recursion function 
'''we know that a function can call other functions. it is even possible for the function
 to call itself these type of construct are termed as recursion function '''
def factorial(x):
    if (x==1 or x==0):
        return 1
    else:
        return x*factorial(x-1)
print(factorial(4))

# Quick quiz:write a program to print the fibonacci sequence

def fibonacci(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(0))
