from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.L_side = 0
        self.R_side = 0
        self.update_score()

    def l_score(self):
        self.L_side += 1
        self.update_score()

    def r_score(self):
        self.R_side += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 240)
        self.write(self.L_side, align="center", font=("courier", 40, "normal"))
        self.goto(100, 240)
        self.write(self.R_side, align="center", font=("courier", 40, "normal"))    
        

