from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor()
screen.title("My Snake Game")
screen.tracer(0)


screen.exitonclick()

snake = Snake()

screen.listen()

screen.onkey(snake.up(), "Up")
screen.onkey(snake.down(), "Down")
screen.onkey(snake.left(), "Left")
screen.onkey(snake.right(), "Right")

screen.update()

