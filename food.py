from turtle import Turtle, Screen
import random

ONESTEP = 20
RANGE = 10
MINUSRANGE = -10

class Food(Turtle):
    def __init__(self, not_allow_list):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.position = {}
        self.refresh(not_allow_list)

    def refresh(self, not_allow_list):
        self.is_pos_not_ok = True
        while self.is_pos_not_ok:
            self.position["x"] = random.randint(MINUSRANGE, RANGE) * ONESTEP
            self.position["y"] = random.randint(MINUSRANGE, RANGE) * ONESTEP
            if self.position not in not_allow_list:
                self.is_pos_not_ok = False
        self.goto(self.position["x"], self.position["y"])

    def get_position(self):
        return self.position
