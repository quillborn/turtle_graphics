from turtle import Turtle

up=90
down=270
left=180
right=0

class Snake:
    def __init__(self):
        self.segment_list = []
        self.create_snake(3)

    def create_snake(self, length):
        x = 0
        y = 0
        for n in range(length):
            segment = Turtle()
            segment.penup()
            segment.shape("square")
            segment.color("white")
            segment.goto(x,y)
            self.segment_list.append(segment)
            x -= 20

    def move(self, distance):
        for seg_num in range(len(self.segment_list)-1, 0, -1):
            new_x = self.segment_list[seg_num - 1].xcor()
            new_y = self.segment_list[seg_num - 1].ycor()
            self.segment_list[seg_num].goto(new_x, new_y)
        
        self.segment_list[0].forward(distance)

    def up(self):
        if self.segment_list[0].heading() != down:
            self.segment_list[0].setheading(up)

    def down(self):
        if self.segment_list[0].heading() != up:
            self.segment_list[0].setheading(down)

    def left(self):
        if self.segment_list[0].heading() != right:
            self.segment_list[0].setheading(left)

    def right(self):
        if self.segment_list[0].heading() != left:
            self.segment_list[0].setheading(right)