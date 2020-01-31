import math

def mysqrt(a):
    # let the initial guess value equals to 0.5 times a
    x = a*0.5
    while True:
        #print(x)
        y = (x+a/x)/2.0
        if y==x:
            return y
            break
        x = y

def test_square_root(a_list):
    #print first two rows
    line1a = "a"
    line1b = "mysqrt(a)"
    line1c = "math.sqrt(a)"
    line1d = "diff"
    
    line2a = "-"
    line2b = "---------"
    line2c = "------------"
    line2d = "----"
    
    spacing1 = " "
    spacing2 = " " * 3
    spacing3 = ""
    
    print(line1a, spacing1, line1b, spacing2, line1c, spacing3, line1d)
    print(line2a, spacing1, line2b, spacing2, line2c, spacing3, line2d)   
    # print the list of sqaure root value of different a
    for a in a_list:
        c2 = mysqrt(a)
        c3 = math.sqrt(a)
        c4 = abs(mysqrt(a) - math.sqrt(a))
        print("{:.1f}".format(a), "{:.11f}".format(c2), "{:.11f}".format(c3), c4)

test_square_root(range(1,10)) 