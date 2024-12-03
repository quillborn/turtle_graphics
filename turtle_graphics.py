import turtle as t
import turtle
import random
import colorgram
from turtle_race import turtle_race

turtle.colormode(255)
screen = t.Screen()
dribble = t.Turtle()
dribble.shape("turtle")
dribble.color("green")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # print(f"{r},{g},{b}")
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
                q = input("continue random walk? Y/N")
                if q == "y":
                    counter = 0
                    break
                elif q == "n":
                    return
                else:
                    continue

def spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        dribble.color(random_color())
        dribble.speed(0)
        dribble.circle(100)
        dribble.setheading(dribble.heading() + size_of_gap)
    
    
def color_extract(image,colors):
    """Uses the colorgram package to extract the specified number of colors from the provided image"""
    rgb_colors = []
    colors = colorgram.extract(image,colors)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r,g,b)
        rgb_colors.append(new_color)


hirst_color_list = [(243, 236, 68), (183, 75, 21), (228, 154, 7), (234, 72, 134), (200, 163, 114), (216, 228, 238),
         (202, 131, 191), (116, 168, 241), (220, 231, 5), (76, 173, 37), (71, 103, 230), (125, 205, 126),
           (45, 111, 39), (75, 37, 30), (151, 74, 156), (60, 100, 153), (241, 162, 196), (244, 55, 28), (187, 28, 12),
             (203, 13, 78), (140, 216, 237), (248, 170, 166), (76, 67, 47), (148, 185, 244), (159, 212, 173), (253, 10, 4), 
             (42, 90, 32), (98, 141, 146), (96, 15, 16), (46, 54, 199), (255, 5, 7)]

def dotted_line(size,color_list,paces):
    """creates a dotted line from left to right"""
    for n in range (size):
        dribble.penup()
        dribble.forward(paces)
        color = random.choice(color_list)
        dribble.pendown()
        dribble.dot(20,color)

def tp(x,y):
    """teleports the turtle by lifting up & putting down pen"""
    dribble.hideturtle()
    dribble.penup()
    dribble.speed(0)
    dribble.goto(x,y)
    dribble.pendown()

def hirst_painting(size, color_list, paces):
    """Creates a Hirst style painting using the provided color list"""
    #size = width & height
    #paces = steps between dots
    x = size * -30
    y = size * -30
    tp(x,y)
    for r in range(9):
        dotted_line(size,color_list,paces)
        y += paces
        tp(x,y)

def forward():
    """Turtle moves forwards"""
    dribble.forward(10)

def backwards():
    """Turtle moves backwards"""
    dribble.back(10)

def turn_right():
    """Turtle turns to right"""
    dribble.right(10)

def turn_left():
    """Turtle turns to left"""
    dribble.left(10)

def reset():
    """resets screen"""
    dribble.clear()
    dribble.penup()
    dribble.home()
    dribble.pendown()
    dribble.color(random_color())


def etch_a_sketch():
    dribble.color(random_color())
    screen.listen()
    screen.onkeypress(key = 'w', fun = forward)
    screen.onkeypress(key = 's', fun = backwards)
    screen.onkey(key = 'd', fun = turn_right)
    screen.onkey(key = 'a', fun = turn_left)
    screen.onkey(key = 'space', fun = reset)

while True:
    while True:
        prompt = input("Turtle can perform the following:\nRandom Walk[R], Spirograph[S], Hirst Painting[H], Etch-a-sketch[E], Turtle Race[T]:  ").lower()
        if prompt in ['r', 's', 'h','e','t']:
            break
        else: continue

    if prompt == 'r':
        random_walk()
        break
    elif prompt == 's':
        spirograph(5)
        break
    elif prompt == 'h':
        hirst_painting(10,hirst_color_list,50)
        break
    elif prompt == 'e':
        etch_a_sketch()
        break
    elif prompt == 't':
        dribble.hideturtle()
        turtle_race()
        break

print("Turtle Graphics will exit on click")
screen.exitonclick()
exit()