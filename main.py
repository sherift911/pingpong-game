from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
L_paddle = Paddle((-350,0))
R_paddle = Paddle((350,0))
ball = Ball()
score = Scoreboard()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PingPong")
screen.tracer(0)
screen.listen()
screen.onkey(R_paddle.move_up, "Up")
screen.onkey(R_paddle.move_down, "Down")
screen.onkey(L_paddle.move_up, "w")
screen.onkey(L_paddle.move_down, "s")

default_sleep = 0.1
game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)
    ball.goto(ball.xcor() + ball.x_move, ball.ycor() + ball.y_move)

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.y_move *= -1

    if (ball.xcor() >= 330 and ball.distance(R_paddle) <= 50) or (ball.xcor() <= -330 and ball.distance(L_paddle) <= 50) :
        ball.x_move *= -1 
        default_sleep *= 0.9 

    #right side
    if ball.xcor() > 420:
        ball.goto(0, 0)
        ball.x_move *= -1
        default_sleep = 0.1
        score.l_score()

    #left side
    if ball.xcor() < -420:
        ball.goto(0, 0)
        ball.x_move *= -1
        default_sleep = 0.1
        score.r_score()












screen.exitonclick()










