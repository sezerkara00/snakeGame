from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh([])

    def refresh(self, snake_segments):
        is_safe = False
        while not is_safe:
            is_safe = True
            random_x = random.randint(-280, 280)
            random_y = random.randint(-280, 280)
            
            for segment in snake_segments:
                if segment.distance(random_x, random_y) < 20:
                    is_safe = False
                    break
            
            if is_safe:
                self.goto(random_x, random_y) 