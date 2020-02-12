import turtle
pen=turtle.Turtle()
length=200
for i in range(10):
    for i in range(4):
        pen.forward(length)
        pen.left(90)
    pen.penup()
    pen.forward(5)
    pen.left(90)
    pen.forward(5)
    pen.right(90)
    pen.pendown()
    length=length-20
turtle.done()
