import random
import turtle as t

tim = t.Turtle()
screen = t.Screen()

# tim.color("blue")
# tim.shapesize(5)
tim.pensize(2)
random.seed(200)
screen.colormode(255)


def shape(shape_side_n,color):
    """Create shape of different side angle with different color"""
    angle = 360/shape_side_n
    tim.color(color)
    for _ in range(shape_side_n):
        tim.fd(80)
        tim.right(angle)

for bisect_angle in range(3,10):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    shape(bisect_angle,(r,g,b))







screen.exitonclick()
