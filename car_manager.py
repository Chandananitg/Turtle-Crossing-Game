from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 3
move_dist = STARTING_MOVE_DISTANCE

class CarManager(Turtle):
    def __init__(self):
        super(CarManager, self).__init__()
        self.penup()
        self.shape("square")
        new_y = random.randint(-11, 11)
        ycor = new_y * 20
        self.goto(300, ycor)
        self.color("black", random.choice(COLORS))
        self.shapesize(stretch_len=2, outline=2.5)
        self.setheading(180)

    def move_car(self):
        global move_dist
        self.forward(move_dist)

    def speed_car(self):
        global move_dist
        move_dist += MOVE_INCREMENT
