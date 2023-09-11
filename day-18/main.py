from turtle import Turtle, Screen
import random
#turle module

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("green")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# tkinter module
#GUI - Graphical User Interface 

#Practice Reading Documentation 

tortol = Turtle()
tortol.shape("turtle")
tortol.color("green")
tortol.pensize(15)
tortol.speed("fastest")
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "Violet", "Red", "Blue", "Green", "LightSeaGreen", "wheat", "SlateGray"]
directions = [0, 90, 180, 270]

for _ in range(100):
    tortol.color(random.choice(colors))
    tortol.forward(30)
    tortol.setheading(random.choice(directions))
    

screen = Screen()
screen.exitonclick()