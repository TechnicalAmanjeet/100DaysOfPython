from turtle import Screen , Turtle
import time
from snake import Snake



screen = Screen()
screen.bgcolor("black")
screen.setup(width=600 , height=600)
screen.title("Amanjeet's Snake Game!")
screen.tracer(0) # Turn off the animation for this screen.

snake = Snake()
screen.update() # turn on the animation.

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.tracer(0)
    snake.move()
    screen.update()
    time.sleep(0.1)






screen.exitonclick()