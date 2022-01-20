import time

'''🤩This is slightly different from the course. This is a one player game. 
The ball will be bounced off the left side of the wall. If the user misses the ball, end of game.
if user hits ball, score +1.'''

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

game_scoreboard = Scoreboard()

right_paddle = Paddle(360, 0)
screen.onkey(fun=right_paddle.move_up, key='Up')
screen.onkey(fun=right_paddle.move_down, key="Down")

# this is a one user game so left paddle wont be necessary
# left_paddle = Paddle(-360, 0)
# screen.onkey(fun=left_paddle.move_up, key='s')
# screen.onkey(fun=left_paddle.move_down, key='z')

ball = Ball()

game_on = True

while game_on:
    screen.update()
    # time.sleep(0.1)

    # if ball touches wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    if ball.xcor() <= -380:  # One user player so the other wall is also bounce-able.
        ball.bounce_x()

    # if ball touches paddles_right
    if ball.distance(right_paddle) < 50 and ball.xcor() > 350:
        ball.increase_speed()  # ❗️If this statement is after ball.bounce then the ball will act weird️
        ball.bounce_x()
        game_scoreboard.update_score()

    # # if ball touches paddles_left
    # if ball.distance(left_paddle) < 30 and ball.xcor() > -370:
    #     ball.bounce_x()

    # if ball passes paddle without touching/ out of bounds
    if ball.xcor() >= 380:  # or ball.xcor() <= -380:
        game_on = False
    ball.move()

screen.exitonclick()
