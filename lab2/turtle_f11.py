import turtle
import numpy as np


def circle(r):
    '''
    draws a circle
    :param r: radius
    :return: circle
    '''
    for i in range(0, 360):
        turtle.forward(np.pi * r / 180)
        turtle.left(1)
    for i in range(0, 360):
        turtle.forward(np.pi * r / 180)
        turtle.right(1)


turtle.speed(0)

n = 3
turtle.left(90)
for i in range(n):
    circle(40 + 9 * i)
