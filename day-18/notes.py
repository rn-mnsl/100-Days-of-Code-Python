# How to Import Modules in Python 

from turtle import Turtle, Screen
from random import choice

tortol = Turtle()
tortol.shape("turtle")
tortol.color("green")

for _ in range(4):
    tortol.forward(100)
    tortol.right(90)



tortol = Turtle()
tortol.shape("turtle")
tortol.color("green")

for _ in range(10):
    tortol.color("black")
    tortol.forward(10)
    tortol.color("white")
    tortol.forward(10)
    tortol.color("black")

# or 

for _ in range(10):
    tortol.forward(10)
    tortol.penup()
    tortol.forward(10)
    tortol.pendown()

num_sides = 3

for _ in range(7):
    angle = 360 / num_sides

    #draw the shape 
    for _ in range(num_sides): 
        tortol.forward(100)
        tortol.right(angle)
    
    num_sides += 1

    # tortol.colormode(randint(0, 255))


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed"]
def draw_shape(num_sides):
    angle = 360 / num_sides 
    for _ in range(num_sides):
        tortol.forward(100)
        tortol.right(angle)
        

for shape_side in range(3, 11):
    draw_shape(shape_side)
    tortol.color(choice(colors))