from turtle import Turtle


class SafeSide(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('green')
        self.shapesize(stretch_wid=1, stretch_len=30)
        self.goto(0, 270)
