import turtle

tim = turtle.Turtle()
screen = turtle.Screen()

def up():
    tim.setheading(90)
    tim.fd(10)

def down():
    tim.setheading(270)
    tim.fd(10)

def right():
    tim.setheading(0)
    tim.fd(20)

def left():
    tim.setheading(180)
    tim.fd(20)

def angle():
    tim.right(10)
    tim.fd(2)

screen.onkey(up,"Up")
screen.onkey(down,"Down")
screen.onkey(left,"Left")
screen.onkey(right,"Right")
screen.onkey(angle,"a")

screen.listen()




screen.exitonclick()