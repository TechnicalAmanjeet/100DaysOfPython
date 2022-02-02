import time
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(1)
        # self.goto(-500, 0)

    def move(self, first, second):
        x_cor = 0
        y_cor = 0
        if first == "up":
            y_cor = self.ycor() + 10
        if first == "down":
            y_cor = self.ycor() - 10
        if second == "right":
            x_cor = self.xcor() + 10
        if second == "left":
            x_cor = self.xcor() - 10

        self.goto(x_cor, y_cor)





        # print(self.ycor())
        time.sleep(0.05)
