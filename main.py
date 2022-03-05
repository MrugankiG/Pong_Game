from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from boundary import Boundary
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG ")
screen.tracer(0)


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()
dashed_line = Boundary()

screen.listen()
screen.onkeypress(fun=left_paddle.up, key="w")
screen.onkeypress(fun=left_paddle.down, key="s")
screen.onkeypress(fun=right_paddle.up, key="Up")
screen.onkeypress(fun=right_paddle.down, key="Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with the right and left paddle
    if ball.xcor() > 320 and ball.distance(right_paddle) < 50 or \
            ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        print(ball.xcor())
        ball.bounce_x()

    # if the right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        score.left_point()

    # if the left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        score.right_point()

screen.exitonclick()
