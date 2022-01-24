import turtle as t

tim = t.Turtle()
screen = t.Screen()

tim.color("blue")
# tim.shapesize(5)
tim.pensize(2)


for bisect_angle in range(3,10):
    for move in range(bisect_angle):
        tim.fd(90)
        tim.right(360/bisect_angle)







screen.exitonclick()
