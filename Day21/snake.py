from turtle import Turtle

# constant
INITIAL_POSITION = [(0, 0), (-20, 0), (-40, 0)]
SEGMENT_SQUARE = []
SNAKE_HEADING = [0, 90, 180, 270]
SQUARE_SIZE = 20

class Snake:

    def __init__(self):
        self.create_snake()


    def create_snake(self):
        """It Creates Initial snake with intial position."""
        for position in INITIAL_POSITION:
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(position)
            SEGMENT_SQUARE.append(segment)

    def move(self):
        """It will move the snake forword by 20. i.e
        position of 3nd square => position of 2nd.
        postion of 2nd square => positoion of 1st.
        position of 1st will fd by 20"""

        for seg in range(len(SEGMENT_SQUARE) - 1, 0, -1):
            x_cor = SEGMENT_SQUARE[seg - 1].xcor()
            y_cor = SEGMENT_SQUARE[seg - 1].ycor()
            SEGMENT_SQUARE[seg].goto(x_cor, y_cor)
        SEGMENT_SQUARE[0].fd(20)

    def up(self):
        if not SEGMENT_SQUARE[0].heading() == SNAKE_HEADING[3]:
            SEGMENT_SQUARE[0].setheading(SNAKE_HEADING[1])


    def down(self):
        if not SEGMENT_SQUARE[0].heading() == SNAKE_HEADING[1]:
            SEGMENT_SQUARE[0].setheading(SNAKE_HEADING[3])


    def left(self):
        if not SEGMENT_SQUARE[0].heading() == SNAKE_HEADING[0]:
            SEGMENT_SQUARE[0].setheading(SNAKE_HEADING[2])


    def right(self):
        if not SEGMENT_SQUARE[0].heading() == SNAKE_HEADING[2]:
            SEGMENT_SQUARE[0].setheading(SNAKE_HEADING[0])


