import math
import turtle

def arc(t, r, theta):
# t:turtle, r:radius, theta: angle
    arc_length  = 2 * math.pi * r * abs(theta) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_theta  = float(theta) / n
    t.lt(step_theta/2)
    polyline(t, n, step_length, step_theta)
    t.rt(step_theta/2)

def polyline(t, n, length, theta):
# t: turtle, n: number of petals, length: length of each segment, theta: angles of arcs
    for i in range(n):
        t.fd(length)
        t.lt(theta)

def petal(t, r, theta):
# each petal has two arcs
# t: turtle, r: radius of the arcs, theta: angles of arcs
    for i in range(2):
        arc(t, r, theta)
        t.lt(180.0-theta)


def flower(t, n, r, theta):
# t: turtle, n: number of petals, r: radius of the arcs, theta: angles of arcs
    for i in range(n):
        petal(t, r, theta)
        t.lt(360.0/n)


def move(t, length):
 # move turtle along the trail
    t.pu()
    t.fd(length)
    t.pd()


T = turtle.Turtle()
# draw a sequence of three flowers, as shown in the book.

move(T, -150)
flower(T, 7, 60.0, 60.0)

move(T, 150)
flower(T, 10, 40.0, 80.0)

move(T, 150)
flower(T, 20, 140.0, 20.0)

T.hideturtle()
turtle.mainloop()
turtle.bye()
