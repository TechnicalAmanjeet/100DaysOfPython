import turtle
from turtle import *

screen = turtle.Screen()

def f():
    setheading(90)
    fd(50)

screen.onkey(f, "Up")
screen.listen()


screen.exitonclick()