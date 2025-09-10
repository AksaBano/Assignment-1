# Task 1: Calculate Factorial Using a Function 


# Problem Statement: Write a Python program that:
# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# 2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output.

def factorial (n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
sample_number= int (input("Enter a number:"))
result= factorial(sample_number)
print (f"factorial of 6 is:", result)

# Answer Task 1:
Enter a number:6
factorial of 6 is: 720

# Task 2: Using the Math Module for Calculations
 
# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
#  Square root of the number
# Natural logarithm (log base e) of the number
# Sine of the number (in radians)
# 3.   Displays the calculated results.

import math
def calculate_and_display_math_functions():
    if a>0:
        square_root= math.sqrt(a)
        print("square root:" ,square_root)
    elif a>0:
        natural_logarithm = math.log(a)
        print ("logarithm:", natural_logarithm)
    elif a>0:
        sine_value= math.sin(a)
        print ("sine:", sine_value)
    else:
        print ("Invalid Input")
a= int (input ("Enter a number: "))
b= math.sqrt(a)
c= math.log (a)
d= math.sin(a)
print (f"Square root:", b)
print (f"Logarithm:", c)
print (f"Sine:", d)

Answer task 2
Enter a number: 49
Square root: 7.0
Logarithm: 3.8918202981106265
Sine: -0.9537526527594719





 