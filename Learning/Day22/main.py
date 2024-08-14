# Exercitiul 1

from turtle import Screen, Turtle
from scoreboard import Scoreboard
from paddle import Paddle, draw_net
from ball import Ball
import time

# TODO : Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Jocul Pong")
screen.tracer(0)

draw_net()

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(l_paddle.move_up, "Up")
screen.onkey(l_paddle.move_down, "Down")
screen.onkey(r_paddle.move_up, "w")
screen.onkey(r_paddle.move_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position("left")
        scoreboard.l_point()
        
    # Detect when left paddle missess
    if ball.xcor() < -380:
        ball.reset_position("right")
        scoreboard.r_point()
    
    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        game_is_on = False
        scoreboard.game_over()
    

screen.exitonclick()