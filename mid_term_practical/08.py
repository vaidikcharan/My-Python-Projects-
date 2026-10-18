#Find the Maximum of two numbers in Python

#Given two numbers, the task is to find the greater number among them. For example:
#Input: a = 10, b = 8
#Output: 10

print("Using max(): ")
a= 5
b= 10
print(max(a, b))


print("Using max(): ")
print(a if a>b else b)


print("Using if-Else statement: ")
p= 60
q= 50

if(p > q):
    print(f"{p} is greater.")
else: 
    print(f"{q} is greater.")
