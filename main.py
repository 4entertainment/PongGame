import time
from turtle import Screen
import random
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Pong Game")

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle_r
    if ball.distance(paddle_r) < 50 and ball.xcor() > 340:

        ball.bounce_x()
    # detect collision with paddle_l
    if ball.distance(paddle_l) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:

        ball.bounce_x()

    # detect R paddle misses
    if ball.xcor() > 350:
        ball.reset_position()
        scoreboard.l_point()
    # detect L paddle misses
    if ball.xcor() < -350:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
