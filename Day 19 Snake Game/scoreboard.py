from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Copperplate', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color('white')
        self.print_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.print_score()

    def print_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def print_game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER!! TOTAL Score: {self.score}", align=ALIGNMENT, font=FONT)
