from turtle import Turtle

MOVE_DISTANCE = 20


class GameTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.go_to_start_position()
        self.left(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start_position(self):
        self.goto(0, -280)
