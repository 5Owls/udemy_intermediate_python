from turtle import Turtle

SNAKE_START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        # attributes of snake
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.body = self.snake[2:]
        self.tail = self.snake[len(self.snake)-1]

    # functionality of snake
    def create_snake(self):
        for i in range(0, 3):
            snake_piece = Turtle()
            snake_piece.penup()
            snake_piece.shape('square')
            snake_piece.color('white')
            snake_piece.goto(SNAKE_START_POSITION[i])
            self.snake.append(snake_piece)

    def extend_snake_body(self):
        snake_piece = Turtle()
        snake_piece.penup()
        snake_piece.shape('square')
        snake_piece.color('white')
        snake_piece.goto(self.tail.position())
        self.snake.append(snake_piece)


    def move(self):
        # Move snake forward by 20 pixels
        # for segment in snake:
        #     segment.forward(20)
        # For every piece in snake, starting from the last piece working to the front
        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
