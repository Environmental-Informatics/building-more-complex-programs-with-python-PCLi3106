def check_fermat(a, b, c, n):
# if n >2, and the formula still works
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

def prompt():
#raw_input() was renamed to input  (PEP 3111)
    a = input("Input a-value:\n")
    b = input("Input b-value:\n")
    c = input("Input c-value:\n")
    n = input("Input n-value:\n")
    a_int = int(a)
    b_int = int(b)
    c_int = int(c)
    n_int = int(n)
    check_fermat(a_int, b_int, c_int, n_int)

prompt()