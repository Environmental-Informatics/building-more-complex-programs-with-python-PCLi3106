"""
Header Comments
File created on 02/05/2020 by Pin-Ching Li for ABE65100

This script is written for drawing flowers by the turtle module

There are three flowers drawn in this scrip by the given number of:
    1. number of petals
    2. radius of the arcs of the petal
    3. the angels of the arcs

These three flowers would be shown and aligned in the same plot 
"""

import math     #import math module for the calcuation tools
import turtle   #import turtle module for drawing purpose

# define the arc in each petal
def arc(t, r, theta):
# t:turtle, r:radius, theta: angle
    # length of arc by the geometric formula 
    arc_length  = 2 * math.pi * r * abs(theta) / 360  
    # step information of a turtle-> speed of the motion of turtle
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_theta  = float(theta) / n
    t.lt(step_theta/2)
    polyline(t, n, step_length, step_theta)
    t.rt(step_theta/2)

# draw the polyline in each arc
def polyline(t, n, length, theta):
# t: turtle, n: number of petals, length: length of each segment, theta: angles of arcs
    #draw polyline with the step information
    for i in range(n):
        t.fd(length)
        t.lt(theta)

# define a function petal to draw each petal
def petal(t, r, theta):
# each petal has two arcs
# t: turtle, r: radius of the arcs, theta: angles of arcs
    for i in range(2):
        arc(t, r, theta)
        t.lt(180.0-theta)

# flower is the function for user to combine the component of numbers of petals
# turtle is a input for the drwaing purpose
def flower(t, n, r, theta):
# t: turtle, n: number of petals, r: radius of the arcs, theta: angles of arcs
    for i in range(n): #n is the numbers of petals needed to be draw
        petal(t, r, theta) # petal function (used to draw a petal) is called
        # the angle of turtle starts changes 
        # in order to make the petal in flowers not overlap
        t.lt(360.0/n)  


def move(t, length):
 # move turtle along the trail
    t.pu()
    t.fd(length)
    t.pd()


T = turtle.Turtle()
# draw three flowers 
# move function is used for turtle to draw flowers in different central location
move(T, -150) 
# call flower function for the first flower and so on...
flower(T, 7, 60.0, 60.0)

move(T, 150)
flower(T, 10, 40.0, 80.0)

move(T, 150)
flower(T, 20, 140.0, 20.0)

T.hideturtle() 
turtle.mainloop() # make turtle work
# finish the drawing and say bye to turtle
turtle.bye()
