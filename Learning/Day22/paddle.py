# TODO : Crearea unui obiect de tip Paddle

from turtle import Turtle

DISTANCE = 40


class Paddle(Turtle):
    
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)
    
    
    def move_up(self):
        new_y = self.ycor() + DISTANCE
        self.goto(self.xcor(), new_y)
        
    
    def move_down(self):    
        new_y = self.ycor() - DISTANCE
        self.goto(self.xcor(), new_y)
        
        
def draw_net():
    net = Turtle()
    net.color("white")
    net.penup()
    net.goto(0, -300)
    net.setheading(90)
    for _ in range(15):
        net.pendown()
        net.forward(20)
        net.penup()
        net.forward(20)
    net.hideturtle()