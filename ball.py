from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def hit_wall(self):
        new_y = self.y_move * (-1)
        self.y_move = new_y

    def hit_the_paddle(self):
        new_x = self.x_move * (-1)
        self.x_move = new_x

    def restart(self):
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10

    def increase_speed_right(self):
        self.x_move += 2

    def increase_speed_left(self):
        self.x_move -= 2









