import turtle


#head
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.fillcolor('grey')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

#eyes
turtle.penup()
turtle.goto(-40, 40)
turtle.pendown()

turtle.fillcolor('green')
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()

turtle.penup()
turtle.goto(40, 40)
turtle.pendown()

turtle.fillcolor('magenta')
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()

#nose
turtle.penup()
turtle.goto(0, 15)
turtle.pendown()

turtle.width(10)
turtle.right(90)
turtle.forward(30)

#mouth
turtle.penup()
turtle.goto(40, -25)
turtle.pendown()

turtle.width(15)
turtle.pencolor('brown')
turtle.left(180)
turtle.circle(40, -180)



