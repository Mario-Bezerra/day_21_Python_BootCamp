from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(position)
        self.clear()
        self.write(f"{self.score}", False, align="center", font=("Arial", 60, "normal"))

    def increase_score(self):
        self.score +=1
        self.clear()
        self.write(f"{self.score}", False, align="center", font=("Arial", 60, "normal"))
