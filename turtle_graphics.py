from turtle import Turtle, Screen
import random

screen = Screen()
dribble = Turtle()
dribble.shape("turtle")
dribble.color("green")

def random_walk():
    """Turtle will paint a random walk path."""
    directions = [0,90,180,270]
    colors = ["red", "blue","green","yellow","orange","purple","pink","brown"]
    dribble.pensize(20)
    dribble.speed(10)

    counter = 0
    while True:
        x = random.choice(directions)
        y = random.choice(colors)
        dribble.color(y)
        dribble.right(x)
        print(x)
        dribble.forward(50)
        counter += 1
        if counter == 50:
            while True:
                q = input("continue? Y/N")
                if q == "y":
                    counter = 0
                    break
                elif q == "n":
                    screen.exitonclick()
                    exit()
                else:
                    continue

random_walk()