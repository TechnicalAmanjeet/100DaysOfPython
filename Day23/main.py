import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# creating object of player
player = Player()

screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True
while game_is_on:
    # check if player touches the finel line then level up by 1.
    if player.is_touch_finish_line():
        print("level up")
    time.sleep(0.1)
    screen.update()
