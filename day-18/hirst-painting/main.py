import turtle as turtle_module 
import random

turtle_module.colormode(255)
tortol = turtle_module.Turtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19)]

tortol.setheading(225)
tortol.forward(250)
tortol.setheading(0)
tortol.speed("fastest")
tortol.penup()
tortol.hideturtle()
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tortol.dot(20, random.choice(color_list))
    tortol.forward(50)

    if dot_count % 10 == 0:
        tortol.setheading(90)
        tortol.forward(50)
        tortol.setheading(180)
        tortol.forward(500)
        tortol.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
