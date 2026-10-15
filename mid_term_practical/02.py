#Q2. Largest of Three Numbers
#Write a Python program to input three numbers and print the largest among them.
n1=int(input("Enter your first number: "))
n2=int(input("Enter your second number: "))
n3=int(input("Enter your third number: "))

if(n1 > n2):
    if (n1 > n3):
        print(f"{n1} is Greatest.")
    else:
        print(f"{n3} is Greatest.")

elif(n2 > n1):
    if(n2 > n3):
        print(f"{n2} is Greatest.")
    else:
        print(f"{n3} is Greatest.")

else:
    print("ERROR!!!!")