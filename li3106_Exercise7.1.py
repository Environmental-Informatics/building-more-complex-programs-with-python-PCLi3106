"""
Header Comments
File created on 02/05/2020 by Pin-Ching Li for ABE65100

This script is written to create the greatest common divisor (GCD) of two numbers.

This divisor aims to find the largest number that divides both numbers with no remainder.

"""

import math

def mysqrt(a):
    # let the initial guess value equals to 0.5 times a
    x = a*0.5
    while True:
        # formula for finding the sqrt value of a step by step
        y = (x+a/x)/2.0
        if y==x:
            return y
            break
        x = y

def test_square_root(a_list):
    #print first two rows
    #the name of columns
    line1a = "a"
    line1b = "mysqrt(a)"
    line1c = "math.sqrt(a)"
    line1d = "diff"
    
    #the lines under the name of columns
    line2a = "-"
    line2b = "---------"
    line2c = "------------"
    line2d = "----"
    #the spaces between lines
    spacing1 = " "
    spacing2 = " " * 3
    spacing3 = ""
    
    print(line1a, spacing1, line1b, spacing2, line1c, spacing3, line1d)
    print(line2a, spacing1, line2b, spacing2, line2c, spacing3, line2d)   
    # print the list of sqaure root value of different (a)
    for a in a_list:
        # the sqrt value obtained from our function
        c2 = mysqrt(a)
        # the sqrt value obtained from math module
        c3 = math.sqrt(a)
        # difference between c2 and c3
        c4 = abs(mysqrt(a) - math.sqrt(a))
        # print the numbers in our prefered format
        print("{:.1f}".format(a), "{:.11f}".format(c2), "{:.11f}".format(c3), c4)

# run our function
test_square_root(range(1,10)) 