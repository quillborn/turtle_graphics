from turtle import Turtle



class Text(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("green")
        with open("data.txt", mode = "r") as file:
            self.high_score = int(file.read())
    
    def update_scoreboard(self):
        self.clear()
        self.goto(0,250)
        self.write(f"Score: {self.score}  High Score: {self.high_score}", True, "center", font = ('Arial',25,'normal'))

    def display_center(self, text):
        self.goto(0,0)
        self.write(text, True, "center", font = ('Arial',25,'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def level_up(self):
        self.score += 1
        self.update_scoreboard()
