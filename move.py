from turtle import Screen
from snake import Snake

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Move:
    def __init__(self):
        self.snake = Snake()
        self.screen = Screen()
        self.screen.listen()
        self.setup_controls()
        
    def setup_controls(self):
        self.screen.onkey(self.move_up, "Up")
        self.screen.onkey(self.move_down, "Down")
        self.screen.onkey(self.move_left, "Left")
        self.screen.onkey(self.move_right, "Right")
    
    def move_up(self):
        if self.snake.segments[0].heading() != DOWN:
            self.snake.segments[0].setheading(UP)
        
    def move_down(self):
        if self.snake.segments[0].heading() != UP:
            self.snake.segments[0].setheading(DOWN)
        
    def move_left(self):
        if self.snake.segments[0].heading() != RIGHT:
            self.snake.segments[0].setheading(LEFT)
        
    def move_right(self):
        if self.snake.segments[0].heading() != LEFT:
            self.snake.segments[0].setheading(RIGHT)
