from turtle import Turtle
import time

STRIP_WIDTH = 1.4
STRIP_LENGTH = 0.2


class MiddleStrip:

    def __init__(self):
        self.create_roadstrip()

    def create_roadstrip(self):
        x_cor = 0
        y_cor = 270

        while not y_cor <= -280:
            tim = Turtle()
            tim.color("white")
            # self.hideturtle()
            tim.penup()
            tim.goto((x_cor, y_cor))
            tim.shape("square")
            tim.shapesize(stretch_wid=STRIP_WIDTH, stretch_len=STRIP_LENGTH)
            y_cor -= 45
