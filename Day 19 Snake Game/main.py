import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 20:
        food.goto_new_position()
        scoreboard.update_score()
        snake.extend_snake_body()

    # Collision with wall
    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or \
            snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        game_is_on = False
        scoreboard.print_game_over()

    # Collision with body
    for segment in snake.body:
        if segment.distance(snake.head) < 20:
            game_is_on = False
            scoreboard.print_game_over()
screen.exitonclick()
