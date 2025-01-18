from turtle import Turtle
import os

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.file_path = os.path.join(os.path.dirname(__file__), "high_score.txt")
        
        # Dosyadan high score'u oku
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                content = file.read().strip()  # Boşlukları temizle
                self.high_score = int(content) if content else 0
        except (FileNotFoundError, ValueError):
            self.high_score = 0
            # Dosyayı düzgün formatta oluştur
            with open(self.file_path, "w", encoding="utf-8") as file:
                file.write("0")
                
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
            with open(self.file_path, "w") as file:
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