import turtle
from food import Food
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    def __init__(self):
        self.segments = []
        self.create_segments()
        self.make_bigger()
        self.head = self.segments[0]

    def create_segments(self):
        for position in STARTING_POSITIONS:
            new_square = turtle.Turtle()
            new_square.shape('square')
            new_square.color('DeepPink')
            new_square.penup()
            new_square.goto(position)
            self.segments.append(new_square)

    def move_snake(self):
        for square_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[square_num - 1].xcor()
            new_y = self.segments[square_num - 1].ycor()
            self.segments[square_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def make_bigger(self):
        last_segment = self.segments[-1]
        new_square = turtle.Turtle()
        new_square.shape('square')
        new_square.color('DeepPink')
        new_square.penup()
        new_square.goto(last_segment.xcor(), last_segment.ycor())  # Place new segment at the last one's position
        self.segments.append(new_square)
