from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scoo = 0
        with open(r'data.txt', "r") as file:
            self.high_score = int(file.read())
        self.goto(-50,300)
        self.penup()
        self.color("yellow")
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score is {self.scoo}, High score is {self.high_score}", move= False, font=("arial", 20, "normal"))

    def reset(self):
        if int(self.scoo) > int(self.high_score):
            self.high_score = self.scoo
            with open(r'D:\100 Days of Code - The Complete Python Pro Bootcamp for 2021\snake_game_alone', mode="w") as file:
                file.write(f"{self.high_score}")
        self.scoo = 0
        self.update()

    def goal(self):
        self.clear()
        self.scoo += 1
        self.update()

