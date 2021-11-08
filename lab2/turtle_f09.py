import turtle as turtle
import numpy as np


def n_polygon(n, R):
    '''
    That fuction draws fine polygon indeed
    :param n: number of angles
    :param R: radius of okruzhnost'
    :return: polygon
    '''
    turtle.left(90 + 180 / n)
    for i in range(n):
        turtle.forward(2 * R * np.sin(np.pi / n))
        turtle.left(360 / n)
    turtle.right(90 + 180 / n)


r = 10
for j in range(3, 13):
    turtle.penup()
    turtle.goto(r, 0)
    turtle.pendown()
    n_polygon(j, r)
    r += 10