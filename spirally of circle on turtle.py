import turtle
pen=turtle.Turtle()
pen.color("red")
pen.speed(2)
for i in range(100):
    pen.circle(5*i)
    pen.circle(-5*i)
    pen.left(i)
turtle.done()
