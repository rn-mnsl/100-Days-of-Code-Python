from turtle import Turtle, Screen

tortol = Turtle()
screen = Screen()


def move_forwards():
    tortol.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()

