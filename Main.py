from turtle import Turtle, Screen

Pawan = Turtle()
screen = Screen()


def move_forwards():
    Pawan.forward(10)

def move_backwards():
    Pawan.backward(10)

def turn_left():
    new_heading = Pawan.heading() + 10
    Pawan.setheading(new_heading)

def turn_right():
    new_heading = Pawan.heading() - 10
    Pawan.setheading(new_heading)

def blank():
    Pawan.penup()

def noblank():
    Pawan.pendown()

def clear():
    Pawan.clear()
    Pawan.penup()
    Pawan.home()
    Pawan.pendown()

screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")
screen.onkey(blank, "b")
screen.onkey(noblank, "n")
screen.exitonclick()
