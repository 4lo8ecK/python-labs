class Point:
    def __init__(self, x: int|float, y: int|float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def move(self, dx: int|float, dy: int|float) -> None:
        self.x += dx
        self.y += dy
    
    def is_origin(self) -> bool:
        return self.x == 0 and self.y == 0
    
    def distance_to(self, point: Point) -> int|float:
        return ((point.x - self.x)**2 + (point.y - self.y)**2) ** (1/2)

p1 = Point(0,0)
p2 = Point(3,4)
print(p1.distance_to(p2))
p2.move(-1, -1)
print(p2)