import random
import colorgram
from turtle import Turtle, Screen

"""Turtle practise. This file contains functions to draw squares, dotted lines, dots with colors extracted from a \n'
 'jpeg file. """

# gram returns a list of colors
gram_colors = colorgram.extract('dot.jpeg', 10)
list_colours = ['red', 'pink', 'brown', 'purple', 'orange', 'green', 'yellow',
                'blue', 'brown4', 'chartreuse4', 'chocolate2', 'coral', 'cornsilk3',
                'IndianRed', 'LavenderBlush3']
list_directions = [0, 90, 180, 270]

screen = Screen()
screen.colormode(255)

# setup turtle
pete_turtle = Turtle()
pete_turtle.color('red')
pete_turtle.pensize(2)
pete_turtle.pendown()
pete_turtle.speed('fastest')


# functions
def draw_line(para_move, para_heading):
    pete_turtle.forward(para_move)
    pete_turtle.setheading(para_heading)


def draw_square():
    for i in range(1, 5):
        move_distance = 100
        heading = 90 * i
        draw_line(move_distance, heading)


def draw_dashed_line():
    pete_turtle.color('black')
    for i in range(0, 4):
        heading = 90
        pete_turtle.setheading(heading * i)
        for k in range(0, 5):
            pete_turtle.forward(10)
            pete_turtle.penup()
            pete_turtle.forward(10)
            pete_turtle.pendown()


def draw_corner_shapes():
    for i in range(3, 10):
        pete_turtle.color(random.choice(list_colours))
        for k in range(0, i):
            pete_turtle.forward(90)
            pete_turtle.right(360 / i)


def random_walk():
    for x in range(0, 50):
        pete_turtle.color(random.choice(list_colours))
        pete_turtle.setheading(random.randint(0, 270))
        pete_turtle.forward(20)


def spirograph():
    for s in range(0, 40):
        red = random.randint(0, 255)
        blue = random.randint(0, 255)
        green = random.randint(0, 255)
        pete_turtle.color(red, blue, green)
        pete_turtle.circle(50)
        pete_turtle.right(10)


def dots():
    pete_turtle.penup()
    for i in range(0, 15):
        x_start_position = -250
        y_start_position = -250 + (i * 20)
        pete_turtle.goto(x_start_position, y_start_position)
        for k in range(0, 15):
            # Dotting in a row
            random_color = random.choice(gram_colors)
            pete_turtle.dot(20, random_color.rgb)
            pete_turtle.forward(40)


screen.exitonclick()
