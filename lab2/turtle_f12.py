import turtle
import numpy as np


def arc(r):
    '''
    arc
    :param r: radius of arc
    :return: im 2 lazy to write this
    '''
    for i in range(0, 180):
        turtle.forward(np.pi * r / 180)
        turtle.right(1)


turtle.speed(0)

n = 3
turtle.left(90)
arc(20)
for i in range(n - 1):
    arc(5)
    arc(20)
