from turtle import Screen
from player import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# creating the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping-Pong Game")
screen.tracer(0)
screen.listen()

# importing the class paddle to create players
r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()

# setup the moves
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# creating the score game
r_score = ScoreBoard((-100, 210))
l_score = ScoreBoard((100, 210))


# loop for the game
game_on = True
while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.hit_wall()

    elif ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.hit_the_paddle()
        ball.increase_speed_left()

    elif ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.hit_the_paddle()
        ball.increase_speed_right()

    elif ball.xcor() > 400:
        r_score.increase_score()
        time.sleep(1)
        r_paddle.back_to_center((370, 0))
        l_paddle.back_to_center((-370, 0))
        ball.restart()

    elif ball.xcor() < -400:
        l_score.increase_score()
        time.sleep(1)
        r_paddle.back_to_center((370, 0))
        l_paddle.back_to_center((-370, 0))
        ball.restart()

screen.exitonclick()
