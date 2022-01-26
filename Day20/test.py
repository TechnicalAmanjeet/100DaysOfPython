import turtle

# Building screen for snake game.
screen = turtle.Screen()
screen.setup(width=500 , height=500)
screen.bgcolor("black")
# screen.title("hlow guy's how are you ")
# turtle.setposition()
# turtle.color("white")
# turtle.write("hlow guy's how are you ")



# Building Snake with 3 white ractangular box.
def make_ractangle():
    # tim.pendown()
    tim.penup()
    tim.color("white")
    tim.begin_fill()
    for _ in range(4):
        tim.fd(10)
        tim.right(90)
    tim.fd(10)
    tim.end_fill()
    return tim.position()


tim = turtle.Turtle()
tim.shapesize(0.001)
tim.shape("circle")



position = make_ractangle()
position = make_ractangle()
position = make_ractangle()
print(position)

screen.exitonclick()