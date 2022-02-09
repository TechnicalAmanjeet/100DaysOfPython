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

car_manage = []
# creating object of car_manager
car = CarManager()
car_manage.append(car)

# create object of scoreboard
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True
no_loops = 0
level = 1
# print(type(car_manage))

while game_is_on:
    # check if player touches the finel line then level up by 1.
    if player.is_touch_finish_line():
        for car in car_manage:
            car.move_increment_fun()
        level += 1
        scoreboard.clear()
        scoreboard.update_level()

    # move each car by some distance
    for car in car_manage:
        # end the game if player hits with the car.
        if car.distance(player) <= 20:
            scoreboard.game_over()
            game_is_on = False

        car.move()
        if car.xcor() == -330:
            car_manage.remove(car)

    time.sleep(0.1)
    screen.update()
    no_loops += 1

    # after every 6 times loop runs create one new object of car.
    if no_loops == 6:
        for i in range(level):
            car = CarManager()
            car_manage.append(car)
        no_loops = 0
        # print(len(car_manage))


screen.exitonclick()
