class Rectangle:
    def __init__(self, width: float|int|None = None, height: float|int|None = None):
        if width == None or height == None:
            raise ValueError("Необходимо ввести и ширину и высоту")
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"Размеры: {self.width}x{self.height}\nПлощадь: {self.area()}\nпериметр: {self.perimeter()}"

    def area(self) -> float|int:
        return self.width * self.height
    
    def perimeter(self) -> float|int:
        return self.width + self.height
    
    def is_square(self, digits: int = 4) -> bool:
        return round(self.width, digits) == round(self.height, digits)

rect = Rectangle(4, 6)
print(rect.area())
print(rect.perimeter())
print(rect)