import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
screen.title("Turtle Crossing")

def level_up():
    global player, scoreboard
    scoreboard.resetlevel()
    player.resetpos()


player = Player()
screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")

game_is_on = True
carlist = []
iteration_no = 1
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for c in carlist:
        c.move_car()
        if player.distance(c) < 20:
            game_is_on = False
            scoreboard.game_over()
            time.sleep(3)
    if player.ycor() > 260:
        level_up()
        carlist[iteration_no].speed_car()
    if iteration_no % 6 == 0:
        new_car = CarManager()
        carlist.append(new_car)
        iteration_no = 1
    iteration_no += 1
