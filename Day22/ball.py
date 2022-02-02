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
        self.goto(-500, 0)

    def move(self):
        if int(self.heading()) == 0:
            if self.ycor() <= 280:
                x_cor = self.xcor() + 10
                y_cor = self.ycor() + 10
                self.goto(x_cor, y_cor)
            else:
                self.setheading(270)
        elif int(self.heading()) == 270:
            if self.ycor() >= -280:
                x_cor = self.xcor() + 10
                y_cor = self.ycor() - 10
                self.goto(x_cor, y_cor)
            else:
                self.setheading(0)

        elif int(self.heading()) == 180:
            x_cor = self.xcor() - 10
            y_cor = self.ycor() + 10
            self.goto(x_cor, y_cor)


        # print(self.ycor())
        time.sleep(0.1)
