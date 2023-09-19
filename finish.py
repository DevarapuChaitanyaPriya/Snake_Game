from turtle import Turtle


class Finish(Turtle):
    def __init__(self):
        super().__init__()
        self.end_game()

    def end_game(self):
        self.hideturtle()
        self.color("red")
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
