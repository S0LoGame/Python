

# Exercitiul 1

# from turtle import Turtle, Screen

# timmy = Turtle() 

# def dotted_line():
#     for _ in range(10):
#         timmy.forward(10)
#         timmy.penup()
#         timmy.forward(10)
#         timmy.pendown()

# def dotted_rectangle():
#     for _ in range(4):
#         dotted_line()
#         timmy.right(90)
        
# dotted_rectangle()
# screen = Screen()
# screen.exitonclick()

# Exercitiul 2
from turtle import Turtle, Screen
import random

colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "brown",
          "cyan", "magenta", "lime", "teal", "navy", "maroon", "olive", "silver",
          "gold", "indigo", "violet", "turquoise", "coral", "plum", "salmon", "khaki",
          "orchid", "peru", "thistle", "chartreuse", "crimson", "sienna"]

timmy = Turtle()
timmy.shape("turtle")
timmy.color(random.choice(colors))
timmy.speed("fastest")

def dotted_line():
    previous_color = None
    for _ in range(10):
        color = random.choice(colors)
        while color == previous_color:
            color = random.choice(colors)
        timmy.color(color)
        timmy.dot(15)  # Draw a dot of size 15
        timmy.penup()
        timmy.forward(15)
        timmy.pendown()
        timmy.penup()
        timmy.forward(15)
        timmy.pendown()
        previous_color = color



def dotted_picture():
    for _ in range(3):
        timmy.pendown()
        dotted_line()
        timmy.left(90)
        timmy.dot(15)
        timmy.penup()
        timmy.forward(30)
        timmy.left(90)
        timmy.pendown()
        dotted_line()
        timmy.right(90)
        timmy.dot(15)
        timmy.penup()
        timmy.forward(30)
        timmy.right(90)    
    timmy.pendown()
    dotted_line()
    timmy.left(90)
    timmy.dot(15)
    timmy.hideturtle()

screen = Screen()
screen.title("Dotted Picture")
screen.setup(width=400, height=400)

timmy.penup()
timmy.goto(-150,-100)
dotted_picture()

screen.exitonclick()

