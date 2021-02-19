from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
move_dist = MOVE_DISTANCE

class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.color("black", "darkslategray")
        self.shapesize(stretch_wid=1, outline=1.5)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.sety(self.ycor()+move_dist)

    def move_down(self):
        self.sety(self.ycor()-move_dist)

    def move_left(self):
        self.setx(self.xcor()-move_dist)

    def move_right(self):
        self.setx(self.xcor()+move_dist)

    def resetpos(self):
        self.goto(STARTING_POSITION)

