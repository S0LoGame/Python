# Inharitance 

# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
        
#     def breathe(self):
#         print("Inhale, exhale")
        
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
        
#     def breathe(self):
#         super().breathe()
#         print("underwater")
        
#     def swim(self):
#         print("moving in water")
        
# nemo = Fish()
# nemo.swim()
# nemo.breathe()
# print(nemo.num_eyes)

# Output:
# moving in water
# Inhale, exhale
# underwater
# 2


# Building Snake Game

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard= Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
        
    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    



screen.exitonclick()
