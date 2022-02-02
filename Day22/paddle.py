import time
from turtle import Turtle

PADDLE_WIDTH = 0.8
PADDLE_LENGTH = 4
UP_MAX = 290
DOWN_MAX = -290

class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        """Take x_cor and y_cor and create paddle at that position
        on the screen."""
        super().__init__()
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.create_paddle()
        print(self.xcor(), self.ycor())

    def create_paddle(self):
        self.color("white")
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH)
        self.setposition(self.x_cor, self.y_cor)
        # print(self.x_cor, self.y_cor)

    def up(self):
        if self.ycor() <= 250:
            self.fd(20)
            print(self.ycor())

    def down(self):
        if self.ycor() >= -250:
            self.fd(-20)
            print(self.ycor())

