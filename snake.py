from turtle import Turtle
UP = 90
DOWN = 270
LEFT= 180
RIGHT = 0

BODY_HALFLEN = 20

class Snake:

    def __init__(self):
        self.turtles = []
        self.turtle_positions = []
        for i in range(0, 3):
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color("purple")
            new_turtle.penup()
            new_turtle.setposition(0 - 20*i, 0)
            self.turtles.append(new_turtle)

    def move(self):
        for num in range(len(self.turtles) - 1, 0, -1):
            if (num == len(self.turtles) - 1):
                self.tail_pos_x = self.turtles[num].xcor()
                self.tail_pos_y = self.turtles[num].ycor()
            new_x = self.turtles[num - 1].xcor()
            new_y = self.turtles[num - 1].ycor()
            self.turtles[num].goto(new_x, new_y)
        self.turtles[0].forward(20)

    def up(self):
        if self.turtles[0].heading() != DOWN:
            self.turtles[0].setheading(UP)

    def down(self):
        if self.turtles[0].heading() != UP:
            self.turtles[0].setheading(DOWN)

    def left(self):
        if self.turtles[0].heading() != RIGHT:
            self.turtles[0].setheading(LEFT)

    def right(self):
        if self.turtles[0].heading() != LEFT:
            self.turtles[0].setheading(RIGHT)

    def is_catch_food(self, food_pos):
        print(f"turtle head pos is [{int(self.turtles[0].xcor())}, {int(self.turtles[0].ycor())}], food pos is [{food_pos['x']}, {food_pos['y']}].")

        if int(self.turtles[0].xcor()) == food_pos["x"] and int(self.turtles[0].ycor()) == food_pos["y"]:
            print("oishi, oishi!")
            return True
        else:
            return False

    def get_body_positions(self):
        for turtle_item in self.turtles:
            pos = {}
            pos["x"] = turtle_item.xcor()
            pos["y"] = turtle_item.ycor()
            self.turtle_positions.append(pos)

        return self.turtle_positions

    def check_outside_border(self, border_x, border_y):
        if abs(self.turtles[0].xcor()) + BODY_HALFLEN > border_x or abs(self.turtles[0].ycor()) + BODY_HALFLEN > border_y:
            return True
        else:
            return False

    def extend(self):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(self.tail_pos_x, self.tail_pos_y)
        self.turtles.append(new_turtle)

