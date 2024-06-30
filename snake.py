

from turtle import Turtle
MOVE_DISTANCE=20

class Snake:
    
    def __init__(self):
        self.all_turtle=[]
        self.width = 0
        self.create_snake()
        self.head=self.all_turtle[0]
    
    def create_snake(self):
        for _ in range(3):
            self.add_turtle()
    
    def add_turtle(self, position=None):
        new_turtle = Turtle("square")
        new_turtle.penup()
        new_turtle.color("white")
        if position:
            new_turtle.goto(position)
        else:
            new_turtle.goto(self.all_turtle[-1].position() if self.all_turtle else (0, 0))
        self.all_turtle.append(new_turtle)
    
    def extend_snake(self):
        # Add a new segment to the end of the snake
        self.add_turtle(self.all_turtle[-1].position())
    
    def move(self):
        for num in range(len(self.all_turtle) - 1, 0, -1):
            new_x = self.all_turtle[num - 1].xcor()
            new_y = self.all_turtle[num - 1].ycor()
            self.all_turtle[num].goto(new_x, new_y)
        
        self.all_turtle[0].forward(MOVE_DISTANCE)
    def go_up(self):
        if self.all_turtle[0].heading() != 270:  # Prevent the snake from reversing
            self.all_turtle[0].setheading(90)

    
    def go_down(self):
        if self.all_turtle[0].heading() != 90:  # Prevent the snake from reversing
            self.all_turtle[0].setheading(270)

    
    def go_left(self):
        if self.all_turtle[0].heading() !=0:
            self.all_turtle[0].setheading(180)
    
    def go_right(self):
        if self.all_turtle[0].heading() !=180:
            self.all_turtle[0].setheading(0)
    