from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # Dosyadan high score'u oku
        try:
            with open("high_score.txt", "r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(0, 300)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # Yeni high score'u dosyaya kaydet
            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.clear()
        self.update_scoreboard()
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
        self.goto(0, -30)
        self.write("Press SPACE to restart", align="center", font=("Courier", 16, "normal")) 