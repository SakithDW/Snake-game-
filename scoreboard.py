from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def load_high_score(self):
        try:
            with open("data.txt") as data:
                return int(data.read())
        except FileNotFoundError:
            with open("data.txt", mode="w") as data:
                data.write("0")  # Default high score
                return 0
        except ValueError:
            return 0  # If file is empty or corrupted, return default value

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score_board(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
