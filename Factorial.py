def factorial(x):
    '''this is a reculsive function to find the factorial of an integer'''

    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

#display the result
print(factorial.__doc__)
print("The factorial of 0 is:", factorial(0))
print("The factorial of 1 is:", factorial(1))
print("The factorial of 2 is:", factorial(2))
print("The factorial of 587 is:", factorial(587))
print("The factorial of 778767653565798098754 is:", factorial(778767653565798098754))