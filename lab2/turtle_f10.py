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


def flower(r, n):
    '''
    draws a flower
    :param r: radius of circles
    :param n: number of petals
    :return: flower ^^
    '''
    for j in range(3):
        circle(r)
        turtle.left(360 / n)


turtle.speed(0)

n = 8
flower(50, n)
