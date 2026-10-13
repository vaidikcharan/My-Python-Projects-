#1 se n tak sum calculate karna.
def total(n):
    if(n==1):
        return 1
    return n + total(n - 1)
print(total(5))

#recursive function countdown(n) likh jo n se 1 tak numbers print kare.
def countdown(n):
    if(n == 1):
        return 1
    print(n)
    return countdown(n-1)
print(countdown(5))


#Factorial of a number
#Write a recursive function to calculate the factorial of a number.
#Example: 5!= 5 x 4 x 3 x 2 x 1

def factorial(n):
    if(n==1):
        return 1
    return n * factorial(n-1)
print(factorial(5))

#Sum of natural numbers
#Write a recursive function that calculates the sum of numbers from 1 to n.
#Example: n = 5
def sum(n):
    if(n == 1):
        return 1
    return n + sum(n - 1)
print(sum(5))

#Fibonacci number
#Write a recursive function to calculate the Fibonacci number at position n, 
#using fib(0) = 0 and fib(1) = 1.
#Expected output: fib(6) = 8
def fib(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    return fib(n-1) + fib(n-2)
print(fib(6))