from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.score=0 
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 21, "normal"))
    def score_increase(self):
        self.score+=1
        self.update_score()
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Courier", 21, "normal"))
    