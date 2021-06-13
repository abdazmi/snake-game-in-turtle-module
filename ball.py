from turtle import Turtle
from random import Random

RAND=300

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(0.7)
        self.goto(x=Random().randint(-RAND,RAND), y=Random().randint(-RAND,RAND))


    def randomize_ball(self):
        self.goto(x=Random().randint(-RAND,RAND), y=Random().randint(-RAND,RAND))
