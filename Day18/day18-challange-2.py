import turtle as t

tim = t.Turtle()
screen = t.Screen()

tim.color("blue")
# tim.shapesize(5)
tim.pensize(5)

tim.penup()
tim.setposition(-320,0)


for _ in range(32):
    tim.pendown()
    tim.fd(10)
    tim.penup()
    tim.fd(10)




screen.exitonclick()
