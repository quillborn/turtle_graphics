from turtle import Screen, Turtle
from snake import Snake
from food import Food
from text import Text
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
scoreboard = Text()
centerline = Text()
score = 0
screen_refresh_rate = 0.1
snake_moving = False

# Function to toggle the movement state
def toggle_pause(): 
    global snake_moving
    snake_moving = not snake_moving
    if snake_moving == False: 
        centerline.display_center('Game Paused')
        snake.hide()
        food.hideturtle()
    else: 
        centerline.clear()
        food.showturtle()
        snake.show()

# Bind keys for snake control and pausing
screen.listen()
screen.onkeypress(key="w", fun=snake.up)
screen.onkeypress(key="s", fun=snake.down)
screen.onkeypress(key="d", fun=snake.right)
screen.onkeypress(key="a", fun=snake.left)
screen.onkeypress(key="space", fun=toggle_pause)

scoreboard.update_scoreboard()
snake.hide()
food.hideturtle()
centerline.display_center('Press Space to Start')

# Game loop
while True:   
    screen.update()
    if snake_moving:  # Only move the snake if the game isn't paused
        time.sleep(screen_refresh_rate)
        snake.move(20)

        #detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.clear() 
            scoreboard.level_up()

        #detect collision with wall or tail
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 or snake.snake_collision():
            screen.update()
            time.sleep(screen_refresh_rate)
            scoreboard.reset()
            snake.reset()

        
    

#game over
#hide all objects and display 'game over'
snake.hide()
food.hideturtle()
screen.update() 
centerline.display_center('Game Over')

#potential to incorperate press space to restart option
screen.onkeypress(key="space", fun= print("gameover. Please click screen to exit"))
 
screen.exitonclick()