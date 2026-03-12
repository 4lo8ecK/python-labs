
class Rectangle:
    def __init__(self,
        x_len: int|float = 1, y_len: int|float = 1,
        x_loc: int|float = 0, y_loc: int|float = 0) -> None:
        
        """
        Подразумевается, что по умолчанию прямоугольник единичный
        и находится в координатах (0;0)
        Координатой прямоугольника является левый нижний угол
        """
        if x_len < 0 or y_len < 0: raise ValueError("Длина стороны должна быть больше нуля")

        self.__x_loc = x_loc
        self.__y_loc = y_loc
    
        self.__x_len = x_len
        self.__y_len = y_len

    def __str__(self) -> str:
        return f"Координаты:\t({self.__x_loc}, {self.__y_loc})\nРазмеры:\t({self.__x_len}, {self.__y_len})"

    def mov(self, new_x: int|float = None, new_y: int|float = None) -> None:
        if new_x != None: self.__x_loc = new_x
        if new_y != None: self.__y_loc = new_y
        
    
    def resize(self, new_x: int|float = None, new_y: int|float = None) -> None:
        if new_x != None: self.__x_len = new_x
        if new_y != None: self.__y_len = new_y

    @staticmethod
    def new_by_two(a: Rectangle, b: Rectangle) -> Rectangle:
        new_x_loc = min(a.__x_loc, b.__x_loc)
        new_y_loc = min(a.__y_loc, b.__y_loc)

        new_x_len = (a.__x_loc + b.__x_loc) - min(a.__x_loc, b.__x_loc)
        new_y_len = (a.__y_loc + b.__y_loc) - min(a.__y_loc, b.__y_loc)

        return Rectangle(x_len=new_x_len, y_len=new_y_len, x_loc=new_x_loc, y_loc=new_y_loc)
        pass

    @staticmethod
    def intersection(a: Rectangle, b: Rectangle) -> Rectangle:

        pass

    pass

# int main() :)
if __name__ == "__main__":
    r = Rectangle()
    r1 = Rectangle(2, 5, 1, 3)
    # print(r)
    # print(r1)

    r3 = Rectangle.new_by_two(r, r1)
    print(r3)
    
    pass