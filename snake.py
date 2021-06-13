from turtle import Turtle


class Snake (Turtle):
    def __init__(self):
        super().__init__()
        self.snake_length =[]
        self.X = 0
        for i in range(3):
            self.snake_length.append(Turtle("square"))
            self.snake_length[i].penup()
            self.snake_length[i].color("white")
            self.snake_length[i].goto(x=self.X, y=0)
            self.X -= 20
        self.headOfSnake = self.snake_length[0]

    def move(self):
        for segment in range(len(self.snake_length)-1, 0, -1 ):
            x = self.snake_length[segment-1].xcor()
            y = self.snake_length[segment-1].ycor()
            self.snake_length[segment].goto(x, y)
        self.headOfSnake.forward(20)


    def snake_reset(self):
        for snake in self.snake_length:
            snake.goto(1000,1000)

        self.snake_length.clear()
        self.__init__()


    def turn_left(self):
        self.headOfSnake.setheading(180)

    def turn_right(self):
        self.headOfSnake.setheading(0)

    def downdown(self):
        self.headOfSnake.setheading(270)

    def upup(self):
        self.headOfSnake.setheading(90)

    def extend(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        x = self.snake_length[-1].xcor()
        y = self.snake_length[-1].ycor()
        new_segment.goto(x,y)
        self.snake_length.append(new_segment)