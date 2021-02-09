from turtle import Turtle, Screen

HALF_BORDER_WIDTH = 15


class GameBorder(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        border_boy = Turtle()
        border_boy.hideturtle()
        border_boy.penup()
        border_boy.pencolor("green")
        border_boy.pensize(10)
        border_boy.goto(0 - HALF_BORDER_WIDTH - int(self.width / 2), int(self.height / 2) + HALF_BORDER_WIDTH)
        print(f"border point 1:{border_boy.xcor()}, {border_boy.ycor()}")
        border_boy.pendown()
        border_boy.goto(0 - HALF_BORDER_WIDTH - int(self.width / 2), 0 - HALF_BORDER_WIDTH - int(self.height / 2))
        print(f"border point 2:{border_boy.xcor()}, {border_boy.ycor()}")
        border_boy.goto(int(self.width / 2) + HALF_BORDER_WIDTH, 0 - HALF_BORDER_WIDTH - int(self.height / 2))
        print(f"border point 3:{border_boy.xcor()}, {border_boy.ycor()}")
        border_boy.goto(int(self.width / 2) + HALF_BORDER_WIDTH, int(self.height / 2) + HALF_BORDER_WIDTH)
        print(f"border point 4:{border_boy.xcor()}, {border_boy.ycor()}")
        border_boy.goto(0 - HALF_BORDER_WIDTH - int(self.width / 2), int(self.height / 2) + HALF_BORDER_WIDTH)

