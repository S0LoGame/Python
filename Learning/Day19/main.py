# Exercitiul 1

# from turtle import Turtle, Screen

# tim=Turtle()
# screen=Screen()

# def turn_right():
#     tim.right(10)
    
# def turn_left():
#     tim.left(10)

# def move_forwards():
#     tim.forward(10)


# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="a", fun=turn_left)
# screen.exitonclick()

#Functions as inputs

# def add(n1, n2):
#     return n1+n2

# def subtract(n1, n2):
#     return n1-n2

# def multiply(n1, n2):    
#     return n1*n2

# def divide(n1, n2):
#     return n1/n2

# def calculator(n1, n2, func):
#     return func(n1, n2)

# result=calculator(2, 3, add)
# print(result)
# result=calculator(2, 3, multiply)
# print(result)


# Exercitiul 2

# from turtle import Turtle, Screen

# tim=Turtle()
# screen=Screen()

# def move_forwards():
#     tim.forward(10)
    
# def move_backwards():
#     tim.backward(10)
    
# def turn_right():
#     new_heading=tim.heading()-10
#     tim.setheading(new_heading)
    
# def turn_left():
#     new_heading=tim.heading()+10
#     tim.setheading(new_heading)
    
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
    
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="c", fun=clear)
# screen.exitonclick()


# Exercitiul 3
# Cursa de testoase

from turtle import Turtle, Screen
import random


screen=Screen()
screen.setup(width=500, height=400)

user_bet=screen.textinput(title="Make your bet", prompt="Avaible colors are red, blue, green, yellow, purple \n \t    Which turtle will win : ")

timy=Turtle(shape="turtle")
timy.color("red")
timy.penup()
timy.goto(x=-230, y=-100)

tom=Turtle(shape="turtle")
tom.color("blue")
tom.penup()
tom.goto(x=-230, y=-60)

tina=Turtle(shape="turtle")
tina.color("green")
tina.penup()
tina.goto(x=-230, y=-20)

toto=Turtle(shape="turtle")
toto.color("yellow")
toto.penup()
toto.goto(x=-230, y=20)

trolo=Turtle(shape="turtle")
trolo.color("purple")
trolo.penup()
trolo.goto(x=-230, y=60)

all_turtles=[timy, tom, tina, toto, trolo]

def move(turtle):
    turtle.forward(random.randint(0, 10))

while True:
    for turtle in all_turtles:
        move(turtle)
        if turtle.xcor()>230:
            winner=turtle.pencolor()
            if winner==user_bet:
                print(f"You've won! The winner is {winner}")
            else:
                print(f"You've lost! The winner is {winner}")
            break
    if turtle.xcor()>230:
        break
    
screen.exitonclick()

