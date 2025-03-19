from turtle import Turtle

FONT = ("Courier", 24, "normal")
STARTING_LEVEL = 1


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = STARTING_LEVEL
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.show_scoreboard()

    def show_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.show_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

