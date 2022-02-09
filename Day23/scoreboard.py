from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "left"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.data = "Leval "
        self.level = 1
        self.arg = self.data + str(self.level)
        self.penup()
        self.goto(-280, 250)
        self.write(arg=self.arg, align=ALIGN, font=FONT)
        self.hideturtle()

    def update_level(self):
        self.level += 1
        self.arg = self.data + str(self.level)
        self.write(arg=self.arg, align=ALIGN, font=FONT)

    def game_over(self):
        # self.home()
        self.goto(-80, 0)
        self.write(arg="Game Over!", align=ALIGN, font=FONT)

