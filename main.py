from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Function to toggle game pause
def toggle_pause():
    global game_is_paused
    game_is_paused = not game_is_paused
    if game_is_paused:
        pause_text.clear()  # Clear any previous pause messages
        pause_text.write("Game Paused", align="center", font=("Courier", 24, "normal"))
    else:
        pause_text.clear()  # Clear the pause message when resuming
        pause_text.hideturtle()

# Initialize screen and game objects
my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=600, height=600)
my_screen.title("My Snake Game")
my_screen.tracer(0)  # Turn off automatic screen updates

snake = Snake()
food = Food()
score = Scoreboard()
game_is_on = True
game_is_paused = False  # Initial pause state

# Create a turtle for displaying pause message
pause_text = Turtle()
pause_text.hideturtle()
pause_text.color("white")
pause_text.penup()
pause_text.goto(0, 0)

# Listen for key events
my_screen.listen()
my_screen.onkey(snake.go_up, "Up")
my_screen.onkey(snake.go_down, "Down")
my_screen.onkey(snake.go_left, "Left")
my_screen.onkey(snake.go_right, "Right")
my_screen.onkey(toggle_pause, "Escape")  # Bind "Escape" key to toggle pause

while game_is_on:
    my_screen.update()
    
    if not game_is_paused:
        snake.move()
        
        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.hideturtle()
            food=Food()  # Refresh food position instead of creating a new one
            snake.extend_snake()
            score.score_increase()
        
        # Detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_is_on = False
            score.game_over()

        # Detect collision with tail
        for segment in snake.all_turtle[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                score.game_over()
    
    # Add a short delay to control the speed of the game
    time.sleep(0.2)
    
# Keep the window open until clicked
my_screen.mainloop()
