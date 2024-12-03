from turtle import Turtle, Screen
import random

def turtle_race():
    screen = Screen()
    screen.setup(width=500, height=400)
    while True:
        user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race?\nred, orange, yellow, green, blue, pruple").lower()
        if user_bet in ['red','orange', 'yellow', 'green','blue','purple']:
            break
        else:
            print("Please enter one of the following colors.\nred, orange, yellow, green, blue, pruple.")

    colors = ["red", "orange","yellow","green","blue","purple"]

    # dribble = Turtle(shape = "turtle")
    # dribble.penup()
    # dribble.goto(x=-230, y=-100)
    x = -230
    y = -100
    racers = []

    for n in range(0,6):
        racer = Turtle(shape = "turtle")
        racer.color(colors[n])
        racer.penup()
        racer.goto(x, y)
        y += 40
        racers.append(racer)

    if user_bet:
        race_on = True

    while race_on:
        for racer in racers:
            random_distance = random.randint(0, 10)
            racer.forward(random_distance)
            if racer.xcor() >= 230:
                winning_color = racer.pencolor()
                if racer.pencolor == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                    race_on = False
                else: 
                    print(f"You've Lost! The {winning_color} turtle is the winner!")
                    race_on = False

    screen.exitonclick()