import turtle as t
import turtle
import random

turtle.colormode(255)

screen = t.Screen()
dribble = t.Turtle()
dribble.shape("turtle")
dribble.color("green")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    print(f"{r},{g},{b}")
    c_value = (r,g,b)
    return c_value

def random_walk():
    """Turtle will paint a random walk path."""
    directions = [0,90,180,270]
    dribble.pensize(20)
    dribble.speed(10)

    counter = 0
    while True:
        x = random.choice(directions)
        dribble.color(random_color())
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

def spirograph():
    for i in range(0,73):
        dribble.speed(0)
        dribble.circle(100)
        dribble.right(5)
        dribble.color(random_color())
    
    screen.exitonclick()
    
spirograph()