from turtle import Turtle   

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 260)
        self.write(f"Left: {self.l_score} \t Right: {self.r_score}", align="center", font=("Courier", 24, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Left: {self.l_score} \t Right: {self.r_score}", align="center", font=("Courier", 24, "normal"))

        
        
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
        
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 24, "normal"))
        
    