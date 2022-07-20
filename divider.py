from turtle import Turtle

from constants import SCREEN_HEIGHT


class Divider(Turtle):

    def __init__(self):
        super().__init__()
        self.set_properties()
        self.draw_dashed_line()

    def set_properties(self):
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.setpos(x=0, y=-SCREEN_HEIGHT)
        self.setheading(90)

    def draw_dashed_line(self):
        while self.ycor() <= SCREEN_HEIGHT:
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
