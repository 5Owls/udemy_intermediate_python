import time
from turtle import Screen
from gameturtle import GameTurtle
from safeside import SafeSide
from carmanager import CarManager
from scoreboard import Scoreboard
'''Turtle crosses a very busy road to get to the other side.'''
screen = Screen()
screen.setup(height=600, width=600)
screen.title('Turtle Cross Game')
screen.tracer(0)
screen.listen()

the_safe_side = SafeSide()
the_scoreboard = Scoreboard()
the_car_manager = CarManager()

benny_turtle = GameTurtle()
screen.onkey(fun=benny_turtle.move_up, key='Up')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    the_car_manager.create_car()
    the_car_manager.move()

    for car in the_car_manager.all_cars:
        if benny_turtle.distance(car) < 20:
            game_is_on = False

    # turtle is safe
    if benny_turtle.ycor() > 270:
        the_scoreboard.update_score()
        benny_turtle.go_to_start_position()

screen.exitonclick()
