from turtle import Screen
import time
from snake import Snake
from food import Food
from finish import Finish

score = 0

snake = Snake()
food = Food()
segments = []
my_screen = Screen()
my_screen.setup(600, 600)
my_screen.bgcolor("pink")
my_screen.listen()

my_screen.tracer(0)
my_screen.onkey(snake.up, 'Up')
my_screen.onkey(snake.right, "Right")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.down, "Down")
game_is_on = True
while game_is_on:
    my_screen.update()
    my_screen.title(f"Snake game: Score {score}")
    time.sleep(0.2)
    snake.move()
    if snake.head.distance(food) < 15:
        score += 1
        food.refresh()
        snake.extend()

    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        game_is_on = False
        finish = Finish()

    for i in snake.segments[1:]:
        if snake.head.distance(i) < 10:
            game_is_on = False
            finish = Finish()

my_screen.exitonclick()
