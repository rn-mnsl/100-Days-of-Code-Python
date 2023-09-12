from turtle import Turtle, Screen, home, clearscreen

tortol = Turtle()
screen = Screen()

screen.listen()


def move_forwards():
    tortol.forward(10)

def move_backwards():
    tortol.backward(10)

def rotate_clockwise():
    new_heading = tortol.heading() + 10 
    tortol.setheading(new_heading)


def rotate_counter():
    new_heading = tortol.heading() - 10 
    tortol.setheading(new_heading)

def restart():
    tortol.clear()
    tortol.penup()
    tortol.home()
    tortol.pendown()

angle = 0 
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_clockwise)
screen.onkey(key="d", fun=rotate_counter)
screen.onkey(key="c", fun=restart)

screen.exitonclick()

