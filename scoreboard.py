from turtle import Turtle
FONT = "Courier"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("AliceBlue")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score:{self.score}", False, align="center", font=(FONT, 25, 'normal'))

    def count_food(self):
        self.score += 1
        self.clear()
        self.update_score()

    def print_goodbye(self):
        self.goto(0,0)
        self.write(f"Game Over. Your final score: {self.score}", False, "center",
                         font=(FONT, 25, 'normal'))