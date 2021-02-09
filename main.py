from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from gameborder import GameBorder
import time


turtles = []
is_game_on = True


def end_game():
    global is_game_on
    is_game_on = False

BORDER_WIDTH = 440
BORDER_HEIGHT = 440

screen = Screen()
screen.screensize(BORDER_WIDTH, BORDER_HEIGHT)
screen.bgcolor("black")
screen.title("Ponson's snake game")
screen.tracer(0)

game_border = GameBorder(400, 400)

snake = Snake()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(end_game, "q")

screen.update()


body_list = snake.get_body_positions()
food = Food(body_list)

screen.update()
while is_game_on:
    screen.update()
    time.sleep(0.2)

    snake.move()
    if snake.check_outside_border(int(BORDER_WIDTH / 2), int(BORDER_HEIGHT / 2)):
        print("GAME OVER! Out of the border.")
        score.game_over()
        is_game_on = False

    for segment in snake.turtles[1:]:
        if snake.turtles[0].distance(segment) < 10:
            print("GAME OVER! Oh No! Touched yourself.")
            score.game_over()
            is_game_on = False
            break

    if snake.is_catch_food(food.get_position()):
        score.add_score()
        snake.extend()
        body_list = snake.get_body_positions()
        food.refresh(body_list)


screen.exitonclick()