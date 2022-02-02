import time
from turtle import Screen
from middle_strip import MiddleStrip
from paddle import Paddle
from ball import Ball

WIDTH_SCREEN = 1000
HEIGHT_SCREEN = 600
LEFT_PADDLE_XCOR = -480
LEFT_PADDLE_YCOR = 0
RIGHT_PADDLE_XCOR = 474
RIGHT_PADDLE_YCOR = 0


# creating and defining the screen for pong game.
screen = Screen()
screen.title("Pong Game by Amanjeet!!")
screen.bgcolor("black")
screen.setup(width=WIDTH_SCREEN, height=HEIGHT_SCREEN)
screen.tracer(0)

middle_strip = MiddleStrip()
left_paddle = Paddle(LEFT_PADDLE_XCOR, LEFT_PADDLE_YCOR)
right_paddle = Paddle(RIGHT_PADDLE_XCOR, RIGHT_PADDLE_YCOR)
ball = Ball()

screen.update()

screen.tracer(1)

screen.listen()
# event control for left paddle
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

# event control for right paddle.
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")


# Play game section starts from here.
game_is_on = True

while game_is_on:
    ball.move()

    # if ball will collid with right paddle.
    if right_paddle.distance(ball) <= 15:
        ball.setheading(180)
        print("ram")


screen.exitonclick()
