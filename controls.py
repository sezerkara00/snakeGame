from turtle import Screen, Turtle
from food import Food
from scoreboard import Scoreboard
import time

class Controls:
    def __init__(self, snake):
        self.snake = snake
        self.screen = Screen()
        self.screen.setup(width=600, height=700)
        
        # Oyun alanı sınırlarını çiz
        self.border = Turtle()
        self.border.hideturtle()
        self.border.penup()
        self.border.color("white")
        self.border.goto(-290, -290)
        self.border.pendown()
        for _ in range(4):
            self.border.forward(580)
            self.border.left(90)
        
        # Oyun alanı dışını farklı renk yap
        self.screen.bgcolor("gray20")
        
        # Oyun alanı içini farklı renk yap
        self.game_area = Turtle()
        self.game_area.hideturtle()
        self.game_area.penup()
        self.game_area.color("black")
        self.game_area.goto(-290, -290)
        self.game_area.begin_fill()
        for _ in range(4):
            self.game_area.forward(580)
            self.game_area.left(90)
        self.game_area.end_fill()
        
        self.food = Food()
        self.scoreboard = Scoreboard()
        self.game_is_on = True
        self.screen.listen()
        self.screen.onkey(self.reset_game, "space")

    def check_collision_with_food(self):
        if self.snake.segments[0].distance(self.food) < 15:
            self.food.refresh(self.snake.segments)
            self.snake.extend()
            self.scoreboard.increase_score()
            return True
        return False

    def check_collisions(self):
        # Tüm çarpışma kontrollerini buradan yönetelim
        self.check_collision_with_wall()
        
        if self.check_collision_with_food():
            return True
            
        if self.check_collision_with_self():
            return False
            
        return True

    def check_collision_with_wall(self):
        head = self.snake.segments[0]
        x = head.xcor()
        y = head.ycor()
        
        # Sağ duvardan çıkarsa sol taraftan devam et
        if x > 280:
            head.goto(-280, y)
            
        # Sol duvardan çıkarsa sağ taraftan devam et
        elif x < -280:
            head.goto(280, y)
            
        # Üst duvardan çıkarsa alt taraftan devam et
        elif y > 280:
            head.goto(x, -280)
            
        # Alt duvardan çıkarsa üst taraftan devam et
        elif y < -280:
            head.goto(x, 280)

    def check_collision_with_self(self):
        head = self.snake.segments[0]
        # Baş hariç diğer segmentleri kontrol et
        for segment in self.snake.segments[1:]:
            if head.distance(segment) < 10:
                self.game_is_on = False
                self.scoreboard.game_over()
                return True
        return False

    def reset_game(self):
        if not self.game_is_on:  # Sadece oyun bitmişse reset yapılabilir
            # Yılanı temizle
            for segment in self.snake.segments:
                segment.hideturtle()
            self.snake.segments.clear()
            
            # Yılanı yeniden oluştur
            self.snake.create_snake()
            
            # Yemeği yeniden konumlandır
            self.food.refresh(self.snake.segments)
            
            # Skoru sıfırla
            self.scoreboard.reset()
            
            # Oyunu başlat
            self.game_is_on = True