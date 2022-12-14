from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()

        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 16, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 16, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", move=False, align='center', font=('Arial', 16, 'normal'))


