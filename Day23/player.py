from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        """Move forward 10 unit distance"""
        self.fd(MOVE_DISTANCE)

    def is_touch_finish_line(self):
        """Return True if it touches finish line else Return False"""
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        return False


