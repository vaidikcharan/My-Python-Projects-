#How to Add Two Numbers in Python


#Given two numbers, the task is to add them and display their sum. For Example:
#Input: a = 5, b = 7
#Output: 12

import operator
import math
print("Using + Operator:")
a= 5
b= 7
add= a+b
print(add)

print("Using sum() Function:")
nums= [20, 30,  40]
print(sum(nums))

print("Using sum() Function:")
print(operator.add(50,60))

print("Using math.fsum():")
#The fsum() function from the math module is used for precise floating-point addition.
#It helps reduce rounding errors while adding decimal values.
p= [0.56, 0.3, 0.004]
print(math.fsum(p))