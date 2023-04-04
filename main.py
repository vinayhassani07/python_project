import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move_forward)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.movie_car()

    # detect Collision with the car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on=False
            scoreboard.game_over()

    # successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        cars.level_up()
        scoreboard.increase_level()




screen.exitonclick()
