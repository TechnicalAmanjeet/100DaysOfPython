from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.take_high_score_from_file()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def take_high_score_from_file(self):
        with open("score.txt") as file:
            content = file.read()
            return int(content)


    def update_scoreboard(self):
        self.clear()
        self.write(f"Current Score: {self.score}  High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_high_score_local_file(self, score):
        with open("score.txt", 'w') as file:
            file.write(score)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score_local_file(str(self.score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
