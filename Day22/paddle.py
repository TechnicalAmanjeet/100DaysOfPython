import time
from turtle import Turtle

PADDLE_WIDTH = 4
PADDLE_LENGTH = 0.8
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
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH)
        self.goto((self.x_cor, self.y_cor))

    def up(self):
        """move paddle in upward direction."""
        print(self.xcor(), self.ycor())
        self.color("white")
        self.fd(100)
        print(self.x_cor, self.y_cor)
        print()

    def move(self):
        self.fd(10)
        print("moving forword")
        time.sleep(0.6)