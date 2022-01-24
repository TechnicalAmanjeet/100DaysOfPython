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
    turtle.dot(10,color)
    turtle.penup()
    turtle.forward(15)



# turtle.setworldcoordinates(50,0,1,1)
# turtle.pensize(10)
turtle.penup()
x = -330
y = -270
turtle.setposition(x,y)
print(turtle.position())

for i in range(56):
    for i in range(44):
        generate_scheme()
    y += 15
    turtle.setposition(x,y)







# print(turtle.position())
screen.exitonclick()
