import turtle


def patrick(n):
    if n % 2 == 1:
        turtle.right(90 * (1 - 1 / n))
        for i in range(n):
            turtle.forward(150)
            turtle.right(180 * (1 - 1 / n))
    elif n % 4 == 0:
        turtle.right(90 - 180 / n)
        for i in range(n):
            turtle.forward(150)
            turtle.right(180 - 360 / n)
    else:
        print('Bruh, Im too lazy to think about that')
    turtle.penup()
    turtle.home()
    turtle.pendown()

patrick(5)

turtle.penup()
turtle.goto(200, 0)
turtle.pendown()

patrick(11)
