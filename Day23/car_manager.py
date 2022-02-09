from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POS_X = 330


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.color(random.choice(COLORS))
        starting_pos_y = random.randint(-220, 220)
        self.setposition(STARTING_POS_X, starting_pos_y)
        self.move_increment = STARTING_MOVE_DISTANCE

    def move(self):
        """move car by some distance."""
        self.fd(self.move_increment)
