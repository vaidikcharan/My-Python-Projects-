#Q6. Calculator Using Functions
#Write a Python program to create separate functions for 
#addition, subtraction, multiplication, and division. Perform the operation according to the user's choice.


def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

if(choice == 1):
    print("Result:", add(a, b))
elif (choice == 2):
    print("Result:", subtract(a, b))
elif (choice == 3):
    print("Result:", multiply(a, b))
elif (choice == 4):
    if (b != 0):
        print("Result:", divide(a, b))
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")

    