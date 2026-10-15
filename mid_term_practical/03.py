#Q3. Factorial of a Number
#Write a Python program to calculate the factorial of a given number using a loop.
num= int(input("Enter any number: "))
fac= 1
for i in range(1, num+1):
    fac= fac*i
print(f"Factorial of Given number is: {fac}")
