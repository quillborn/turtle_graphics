from turtle import Screen, Turtle
from snake import Snake
from food import Food
import time

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Initialize the snake and movement state
snake = Snake()
food = Food()
snake_moving = False

# Function to toggle the movement state
def toggle_pause():
    global snake_moving
    snake_moving = not snake_moving

# Bind keys for snake control and pausing
screen.listen()
screen.onkeypress(key="w", fun=snake.up)
screen.onkeypress(key="s", fun=snake.down)
screen.onkeypress(key="d", fun=snake.right)
screen.onkeypress(key="a", fun=snake.left)
screen.onkeypress(key="space", fun=toggle_pause)

# Game loop
while True:
    screen.update()
    if snake_moving:  # Only move the snake if the game isn't paused
        time.sleep(0.1)
        snake.move(20)

        #detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()

screen.exitonclick()