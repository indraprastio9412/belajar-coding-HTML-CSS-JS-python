from turtle import *

def r(x, y):
    rt(x)
    fd(y)

    tracer(5)
    fd(100)
    bgcolor("BLACK")
    color("cyan")
    width(2)

for i in range(2003):
    fd(i)
    r(90, i)
    r(90, i)
    r(270, i)
    r(90, i)
    circle(100,90)
done()