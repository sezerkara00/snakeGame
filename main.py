import turtle
import time
from snake import Snake
from move import Move
from controls import Controls

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Yılan Oyunu")
screen.tracer(0)

move_controller = Move()
snake = move_controller.snake
controls = Controls(snake)

def game_loop():
    while True:
        screen.update()
        time.sleep(0.1)
        
        if controls.game_is_on:
            snake.move()
            controls.check_collisions()
        else:
            screen.update()  # Oyun bitti mesajının görünmesi için ekranı güncelle
            
        screen.update()

game_loop()
screen.exitonclick()


