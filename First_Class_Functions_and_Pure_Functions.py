#Function as a variable
#Write a function square(n) that returns the square of a number. 
#Store the function in another variable called f and call it using f(5).
#Expected output: 25
def square(n):
    return n*n

f= square(5)
print(f)

#Ek function double(n) bana jo number ka double return kare. 
#Phir function ko f variable mein store kar aur f(6) print kar.
def double(n):
    return n*2

d= double
print(d(6))

#Pure function woh function hai jo same input par 
#same output deta hai aur bahar ki value ko change nahi karta.
#example--->>>>
def add(x, y):
    return x+y

print(f"example of pure functions. {add(3, 4)}")
print(f"example of pure functions. {add(5, 10)}")

#Ek pure function multiply(a, b) 
#bana jo dono numbers ka multiplication return kare.
#Example: multiply(4, 5) → 20

def multiply(a, b):
    return a*b

print(multiply(4, 5))

#Create a function calculate(func, a, b) that accepts another function and two numbers. 
#Pass an addition function to calculate the sum of 10 and 20.
#Expected output: 30

def addition(p, q):
    return p+q 

def calculate(func, p, q):
    return func(p, q)
print(calculate(addition, 10, 20))