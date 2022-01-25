import random
import turtle

screen = turtle.Screen()

def create_turtle_object(color,y):
    """Return a turtle object with different color"""
    turtle_obj = turtle.Turtle()
    turtle_obj.color(color)
    turtle_obj.shape("turtle")
    turtle_obj.shapesize(2)
    turtle_obj.penup()
    turtle_obj.setposition(-320,y)
    return turtle_obj

def move_turtle():
    global black_turtle , blue_turtle , red_turtle ,violet_turtle , yellow_turtle
    black_turtle.fd(random.randint(0,10))
    blue_turtle.fd(random.randint(0,10))
    red_turtle.fd(random.randint(0,10))
    violet_turtle.fd(random.randint(0,10))
    yellow_turtle.fd(random.randint(0,10))

def check_position():
    global black_turtle, blue_turtle, red_turtle, violet_turtle, yellow_turtle
    is_true = False
    if black_turtle.position()[0] >= 300:
        is_true = True
        print("Black Turtle wins the race.")
    elif blue_turtle.position()[0] >= 300:
        is_true = True
        print("Blue Turtle wins the race.")
    elif red_turtle.position()[0] >= 300:
        is_true = True
        print("Red Turtle wins the race.")
    elif violet_turtle.position()[0] >= 300:
        is_true = True
        print("Violet Turtle wins the race")
    elif yellow_turtle.position()[0] >= 300:
        is_true = True
        print("Yellow Turtle wins the race")

    return is_true



# creating 6 different type of turtle object
blue_turtle = create_turtle_object("blue",-100)
black_turtle = create_turtle_object("black",-50)
red_turtle = create_turtle_object("red",-0)
violet_turtle = create_turtle_object("violet", 50)
yellow_turtle = create_turtle_object("yellow",100)



while True:
    move_turtle()
    if check_position():
        print("""Thank You so much for playing this game.""")
        break







screen.exitonclick()