from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Cambria', 18, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 250)
        self.score = 0
        self.highscore = self.return_highscore()
        self.write(arg=f"Score: {self.score} HighScore: {self.highscore}", font=FONT, align=ALIGNMENT)

    def update_score(self):
        self.score +=1
        self.clear()
        self.write(arg=f"Score: {self.score} HighScore: {self.highscore}", align=ALIGNMENT, font=FONT)
        self.update_highscore_file()

    def update_highscore_file(self):
        with open("high_score.txt", 'r') as file:
            highscore = int(file.read())
        if self.score > highscore:
            with open("high_score.txt", 'w') as file:
                file.write(str(self.score))

    def return_highscore(self):
        with open('high_score.txt', 'r') as file:
            high_score = file.readline()
        return high_score
