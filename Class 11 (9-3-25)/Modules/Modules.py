# Modules:

# 1. Standard Module

import math

# use a function from the math module
print("To comput the square root")
num = int(input("Enter a number: "))

sqrt = math.sqrt(num)
print(f"The square root of {num} is {sqrt}")


# 2. Importing Specific Functions

from math import sqrt, pow

print("To compute square root and power of given number")

num = int(input("Enter a number: "))

print(f"Square root of {num} is {sqrt(num)}")
print(f"{num} raised to the power of 3 is {pow(num, 3)}")


# 3. Creating and importing your own module as alias in Python
import myModule as mm
# or
#from myModule import multiply, fact

a, b = 2, 3
print(f"{a} x {b} = {mm.multiply(a,b)}")

print(f"Factorial of 5 is {mm.fact(5)}")

p = (2,3)
q = (4,5)
print(f"Distance between two point is {mm.Euclidean_dist(p,q)}")
