def gcd(a, b):
# if b = 0, no remains after the division
    if b == 0:
        return a
    r = a % b
    return gcd(b,r) 

print(gcd(10,5))
