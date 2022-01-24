import random
import turtle

tim = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
tim.speed(10)

# tim.pensize(2)

def draw_shpae(color):
    """Draw circle with different color in diffenent direction"""
    tim.color(color)
    tim.right(-6)
    tim.circle(80)

def color_scheme():
    """Return random tuple set of rgb color"""
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

for _ in range(60):
    color = color_scheme()
    draw_shpae(color)













screen.exitonclick()
