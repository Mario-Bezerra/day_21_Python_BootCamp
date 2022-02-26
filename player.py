from turtle import Turtle

#class paddle ; heranci for Turtle class
class Paddle(Turtle):
    # creating the paddle
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.goto(position)

    # move of the paddles
    def go_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(),new_y)

    def back_to_center(self,position):
        self.goto(position)







