from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.shapesize(0.5, 0.5)
        self.color("DarkCyan")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_pos = random.randint(-280, 280)
        y_pos = random.randint(-280, 280)
        self.goto(x_pos, y_pos)
