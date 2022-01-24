import random
import turtle

# turtle.width = 10
# turtle.ht = 10
# turtle.bgcolor("black")
#
# pen = turtle.pen()
#
screen = turtle.Screen()
screen.screensize(100,200)
screen.colormode(255)
turtle.speed(5000)
# screen.addshape("circle")


# turtle.setworldcoordinates(0,0,2,2)

def make_circle(col):
    turtle.fillcolor(col)
    turtle.begin_fill()
    for i in range(8):
        turtle.forward(1.2)
        turtle.right(45)
        turtle.forward(1.2)
    turtle.end_fill()

def genrate_random_color():
    """ return a tuple of (red,blue,green) color scheme"""
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    return ( red , blue, green)


def generate_scheme():
    """it will make circle and 2 step gets forword"""
    color = genrate_random_color()
    turtle.pendown()
    make_circle(color)
    turtle.penup()
    turtle.forward(10)



# turtle.setworldcoordinates(50,0,1,1)
# turtle.pensize(10)
turtle.penup()
x = -330
y = -270
turtle.setposition(x,y)
print(turtle.position())

for i in range(56):
    for i in range(66):
        generate_scheme()
    y += 10
    turtle.setposition(x,y)

# turtle.pen(fillcolor="black", pencolor="red", pensize=10)
# for i in range(5):
#     turtle.penup()
#     turtle.forward(1)
#     turtle.pendown()
#     turtle.fillcolor("black")





print(turtle.position())
screen.exitonclick()
