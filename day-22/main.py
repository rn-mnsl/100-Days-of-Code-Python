from turtle import Screen, Turtle 
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0)) 
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True 
while game_is_on: 
    time.sleep(0.05)
    screen.update()
    ball.move()

    #Detect Collision with the Wall 
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y() 
        #needs to bounce
    
    #Detect collision with r_paddle 
    if ball.distance(r_paddle) and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


screen.exitonclick()