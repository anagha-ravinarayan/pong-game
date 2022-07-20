from turtle import Turtle

from constants import PADDLE_WIDTH, PADDLE_LENGTH, PADDLE_SPEED


class Paddle(Turtle):

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.set_properties(pos_x, pos_y)

    def set_properties(self, pos_x, pos_y):
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH)
        self.setpos(x=pos_x, y=pos_y)

    def up(self):
        self.setpos(self.xcor(), self.ycor() + PADDLE_SPEED)

    def down(self):
        self.setpos(self.xcor(), self.ycor() - PADDLE_SPEED)
