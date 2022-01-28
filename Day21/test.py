import turtle
from turtle import Screen , Turtle
import time



screen = Screen()
screen.bgcolor("black")
screen.setup(width=600 , height=600)


INITIAL_POSITION = [(0, 0), (-20, 0), (-40, 0)]
SIZE_SQUARE = 20
CURRENT_POSITION = []


for position in INITIAL_POSITION:
    tim = Turtle()
    tim.penup()
    tim.shape("square")
    tim.color("white")
    tim.setposition(position)
    CURRENT_POSITION.append(list(position))
    time.sleep(1)

for position in CURRENT_POSITION:
    CURRENT_POSITION[0][0] = CURRENT_POSITION[0][0] + 20
    CURRENT_POSITION[1][0]





screen.exitonclick()