from turtle import Screen
import turtle as t 
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)

t.speed("fastest")
draw_spirograph(5)


screen = Screen()
screen.exitonclick()