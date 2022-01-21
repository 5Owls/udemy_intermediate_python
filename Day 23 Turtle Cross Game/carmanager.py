import random
from turtle import Turtle

list_colors = ['red', 'blue', 'yellow', 'purple', 'orange', 'brown', 'coral']


class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_number = random.randint(0, 6)
        if random_number == 5:
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(list_colors))
            new_car.penup()
            y_start_position = random.randint(-200, 200)
            new_car.goto(280, y_start_position)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(10)
