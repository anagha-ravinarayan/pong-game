from turtle import Screen
import time

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, TITLE, PADDLE_POSX, PADDLE_POSY, BALL_X_LIMIT, BALL_Y_LIMIT, BALL_PADDLE_DIST, RIGHT, LEFT
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from divider import Divider

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title(TITLE)
screen.tracer(0)

r_paddle = Paddle(PADDLE_POSX, PADDLE_POSY)
l_paddle = Paddle(-PADDLE_POSX, PADDLE_POSY)
ball = Ball()
scoreboard = ScoreBoard()
divider = Divider()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

game_is_on = True
while game_is_on:
    time.sleep(ball.get_move_speed())
    screen.update()
    ball.move()

    # Detect collision with top and bottom walls and bounce
    if ball.ycor() > BALL_Y_LIMIT or ball.ycor() < -BALL_Y_LIMIT:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < BALL_PADDLE_DIST and ball.xcor() > BALL_X_LIMIT and ball.get_paddle_collided() != RIGHT:
        ball.bounce_x(RIGHT)

    # Detect collision with left paddle
    if ball.distance(l_paddle) < BALL_PADDLE_DIST and ball.xcor() < -BALL_X_LIMIT and ball.get_paddle_collided() != LEFT:
        ball.bounce_x(LEFT)

    # Detect ball missed the right paddle
    if ball.xcor() > (SCREEN_WIDTH / 2):
        ball.reset_position()
        scoreboard.increment_l_score()

    # Detect ball missed the left paddle
    if ball.xcor() < -(SCREEN_WIDTH / 2):
        ball.reset_position()
        scoreboard.increment_r_score()

screen.exitonclick()
