from turtle import Turtle


class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.upper()
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.lower()

    def upper(self):
        self.setheading(90)
        self.dashed()

    def lower(self):
        self.setheading(270)
        self.dashed()

    def dashed(self):
        for pace in range(800):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
