
class Rectangle:
    def __init__(self,
        x: int|float = 0, y: int|float = 0,
        width: int|float = 1, height: int|float = 1
        ) -> None:
        
        """
        Подразумевается, что по умолчанию прямоугольник единичный
        и находится в координатах (0;0)
        Координатой прямоугольника является левый нижний угол
        """
        if width < 0 or height < 0: raise ValueError("Длина стороны должна быть больше нуля")

        self.x = x
        self.y = y
    
        self.width = width
        self.height = height

        self.x1 = self.x + self.width
        self.y1 = self.y + self.height

    def __str__(self) -> str:
        return f"Координаты:\t({self.x}, {self.y})\nРазмеры:\t({self.width}, {self.height})"

    def mov(self, new_x: int|float = None, new_y: int|float = None) -> None:
        if new_x != None: self.x = new_x
        if new_y != None: self.y = new_y
        
    
    def resize(self, new_x: int|float = None, new_y: int|float = None) -> None:
        if new_x != None: self.width = new_x
        if new_y != None: self.height = new_y

    @staticmethod
    def do_intersect(a: Rectangle, b: Rectangle) -> bool:
        return (min(a.x1, b.x1) <= max(a.x1, b.x1)) and (min(a.y1, b.y1) <= max(a.y1, b.y1))

        
    @staticmethod
    def new_by_two(a: Rectangle, b: Rectangle) -> Rectangle:

        new_x = min(a.x, b.x)
        new_y = min(a.y, b.y)

        new_width = max(a.x1, b.x1) - min(a.x, b.x)
        new_height = max(a.y1, b.y1) - min(a.y, b.y)

        return Rectangle(width=new_width, height=new_height, x=new_x, y=new_y)

    @staticmethod
    def intersection(a: Rectangle, b: Rectangle) -> Rectangle:
        if Rectangle.do_intersect(a,b):
            wid = max(a.width, b.width) - min(a.width, b.width)
            hght = max(a.height, b.height) - min(a.height, a.width)
            
            x = max(a.x, b.x) - min(a.x, b.x)
            y = max(a.y, b.y) - min(a.y, b.y)

            return Rectangle(x=x, y=y, width=wid, height=hght)
        pass

# int main() :)
if __name__ == "__main__":

    r = Rectangle()
    # r1 = Rectangle(width=2, height=5, x=1, y=3)
    r2 = Rectangle(2, 5, 1, 3)
    
    print(f"r:\n{r}\n")
    # print(f"r1:\n{r1}\n")
    print(f"r2:\n{r2}\n")

    print("Пересечение: ", Rectangle.do_intersect(r, r2))
    # print(Rectangle.new_by_two(r, r2))
    print(Rectangle.intersection(r, r2))

    pass

