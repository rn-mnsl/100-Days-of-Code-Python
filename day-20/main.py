from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Ssnek Game")
screen.tracer(0)
# segment_1 = Turtle("square")
# segment_1.color("white")
# segment_1.goto(0, 0)

# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20, 0)

# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40, 0)

# easier solution 

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True 
while game_is_on: 
    screen.update()
    time.sleep(0.1)

    snake.move()
    
screen.exitonclick()

      
    

        
        








screen.exitonclick()