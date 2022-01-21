from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.retrieve_highscore()
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write(arg=f"Score {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        if self.score >= self.highscore:
            self.update_highscore()
            self.highscore = self.score
        self.clear()
        self.write(arg=f"Score {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def retrieve_highscore(self):
        with open('highscore.txt', 'r') as file:
            int_line = int(file.read())
        return int_line

    def update_highscore(self):
        with open('highscore.txt', 'w') as file:
            file.write(str(self.score))
