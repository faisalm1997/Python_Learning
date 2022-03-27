from shutil import move
from turtle import Turtle, Screen 

tim  = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def turn_left():
    new_heading = tim.heading() + 10 
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()

screen.listen()
screen.onkey(move_forwards, "up")
screen.onkey(move_backwards, "down")
screen.onkey(turn_left, "left")
screen.onkey(turn_right, "right")
screen.onkey(clear, "c")

screen.exitonclick()