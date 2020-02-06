"""
Header Comments
File created on 02/05/2020 by Pin-Ching Li for ABE65100

This script is written to create the greatest common divisor (GCD) of two numbers.

This divisor aims to find the largest number that divides both numbers with no remainder.

"""

def gcd(a, b):
# if b = 0, no remains after the division
    if b == 0:
        return a # remainder equals to zero
    r = a % b # get the remainder
    return gcd(b,r) # the remainder still exists, so we have to do this process again

# print the largest number that divides both numbers with no remainder
print(gcd(10,5))
