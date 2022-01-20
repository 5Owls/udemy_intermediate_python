from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(x_pos, y_pos)
        self.setheading(90)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)
