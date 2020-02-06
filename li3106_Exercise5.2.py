"""
Header Comments
File created on 02/05/2020 by Pin-Ching Li for ABE65100

This script is written for examing the equilibrium formula with the statement of Fermat.

The user can input their numbers into our function and check if the Fermat is right or wrong.

"""

def check_fermat(a, b, c, n):
# if n >2, and the formula still works
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

def prompt():
    # allow user to input the numbers they want to test
    a = input("Input a-value:\n")
    b = input("Input b-value:\n")
    c = input("Input c-value:\n")
    n = input("Input n-value:\n")
    # Because Fermat formula only works for the integer, 
    # we transfer all the inputs into integer 
    a_int = int(a)
    b_int = int(b)
    c_int = int(c)
    n_int = int(n)
    # input all tha values into the formula
    check_fermat(a_int, b_int, c_int, n_int)

# main code, run the function prompt
prompt()