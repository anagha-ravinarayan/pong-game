from turtle import Turtle

from constants import FONT, ALIGNMENT, SCORE_X, SCORE_Y


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.set_properties()
        self.show_score()

    def set_properties(self):
        self.color("white")
        self.penup()
        self.hideturtle()

    def show_score(self):
        self.clear()
        self.setpos(x=-SCORE_X, y=SCORE_Y)
        self.write(arg=self.l_score, align=ALIGNMENT, font=FONT)
        self.setpos(x=SCORE_X, y=SCORE_Y)
        self.write(arg=self.r_score, align=ALIGNMENT, font=FONT)

    def increment_l_score(self):
        self.l_score += 1
        self.show_score()

    def increment_r_score(self):
        self.r_score += 1
        self.show_score()
