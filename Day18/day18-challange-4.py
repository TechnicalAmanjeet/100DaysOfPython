import random
import turtle as t

tim = t.Turtle()
screen = t.Screen()

# tim.color("blue")
# tim.shapesize(5)
tim.pensize(2)
random.seed(200)
screen.colormode(255)
tim.speed(1000)
tim.pensize(10)
# tim.shapesize(10)

angle = [90,180,270,360]
color_rgb = range(0,256)

def random_walk(angle,color):
    tim.right(angle)
    tim.color(color)
    tim.forward(30)

for _ in range(100):
    angle_to_move = random.choice(angle)
    r = random.choice(color_rgb)
    g = random.choice(color_rgb)
    b = random.choice(color_rgb)

    random_walk(angle_to_move,(r,g,b))







screen.exitonclick()
