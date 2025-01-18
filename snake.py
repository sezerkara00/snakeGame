import turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = turtle.Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            
        self.segments[0].forward(20)
        
    def extend(self):
        # Yılanın son segmentinin pozisyonunu al
        tail_position = self.segments[-1].position()
        
        # Yeni segment ekle
        new_segment = turtle.Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(tail_position)
        self.segments.append(new_segment)
        
    def reset(self):
        # Tüm segmentleri temizle
        for segment in self.segments:
            segment.goto(1000, 1000)  # Ekrandan uzaklaştır
        self.segments.clear()
        # Yeni yılan oluştur
        self.create_snake()
        



