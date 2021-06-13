from turtle import Screen
from snake import Snake
import time
from ball import Ball
from score import Score



screen = Screen()
screen.title("snake game")
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
screen.update()
screen.listen()
screen.onkey(key="Up", fun=snake.upup)
screen.onkey(key="Down", fun=snake.downdown)
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)

ball = Ball()
score = Score()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    snake.move()
    if snake.headOfSnake.xcor()> 330 or snake.headOfSnake.xcor() < -330 or\
            snake.headOfSnake.ycor()> 330 or snake.headOfSnake.ycor() < -330:
        score.reset()
        snake.snake_reset()
        time.sleep(1)


    if snake.headOfSnake.distance(ball) <= 20:
        snake.extend()
        score.goal()
        ball.randomize_ball()

    for i in snake.snake_length[1:]:
        if snake.headOfSnake.distance(i) < 10:
            score.reset()
            snake.snake_reset()
            time.sleep(1)



    screen.update()


screen.exitonclick()