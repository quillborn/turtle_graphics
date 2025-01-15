from turtle import Turtle

up=90
down=270
left=180
right=0

class Snake:
    def __init__(self):
        self.segment_list = []
        self.create_snake(3)
        self.head = self.segment_list[0]

    def hide(self):
        for n in self.segment_list:
            n.hideturtle()

    def show(self):
        for n in self.segment_list:
            n.showturtle()

    def create_snake(self, length):
        for n in range(length):
            self.add_segment(0, 0)

    def add_segment(self, x, y):
        segment = Turtle()
        segment.penup()
        segment.shape("square")
        segment.color("white")
        segment.goto(x,y)
        self.segment_list.append(segment)
        x -= 20

    def extend(self):
        self.add_segment(self.segment_list[-1].xcor(), self.segment_list[-1].ycor())

    def snake_collision(self):
        for segment in self.segment_list[1:]:
            if self.head.distance(segment) < 15:
                return True
    


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

    def reset(self):
        for s in self.segment_list:
            s.hideturtle()
            del s
        self.segment_list.clear()
        self.create_snake(3)
        self.head = self.segment_list[0]