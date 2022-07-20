from turtle import Turtle

from constants import BALL_POSX, BALL_POSY, BALL_STEPS, BALL_SLEEP


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.set_properties()
        self.x_move = BALL_STEPS
        self.y_move = BALL_STEPS
        self.move_speed = BALL_SLEEP
        self.paddle_collided = None

    def set_properties(self):
        self.color("white")
        self.penup()
        self.shape("circle")
        self.setpos(x=BALL_POSX, y=BALL_POSY)

    def move(self):
        self.setpos(x=self.xcor() + self.x_move, y=self.ycor() + self.y_move)

    def bounce_x(self, paddle):
        self.x_move *= -1
        self.paddle_collided = paddle
        self.move_speed *= 0.9      # Increase speed of ball after each time it is hit by a paddle

    def bounce_y(self):
        self.y_move *= -1
        self.paddle_collided = None

    def reset_position(self):
        self.setpos(x=BALL_POSX, y=BALL_POSY)
        self.move_speed = BALL_SLEEP
        self.paddle_collided = None
        self.x_move *= -1

    def get_paddle_collided(self):
        return self.paddle_collided

    def get_move_speed(self):
        return self.move_speed
