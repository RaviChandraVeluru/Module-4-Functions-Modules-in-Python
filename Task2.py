'''Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
Square root of the number
Natural logarithm (log base e) of the number
Sine of the number (in radians)
'''

#import math module
from math import *
un = int(input("Enter a number: "))
print("square root: ",sqrt(un))
print("logarithm: ",log(un))
print("sine: ",sin(un))