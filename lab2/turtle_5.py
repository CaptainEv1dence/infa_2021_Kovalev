import turtle


turtle.shape('turtle')
x0 = 10
y0 = 10

for i in range(10):
    turtle.penup()
    turtle.goto(x0 - 10 * i, y0 - 10 * i)
    turtle.pendown()

    for j in range(4):
        turtle.forward(100 + 2 * 10 * i)
        turtle.left(90)


