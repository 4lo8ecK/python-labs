class Trapeze:
    def __init__(self, up: int|float = None, down: int|float = None) -> None:
        if (up == None) or (down == None):
            raise ValueError("Введите оба аргумента")
        if (up < 0) or (down < 0):
            raise ValueError("Значения должны быть положительными")
        self.__up = up
        self.__down = down

    def __str__(self) -> str:
        return f"Длина верхнего основания: {self.__up}\nДлина нижнего основания: {self.__down}\nДлина полусуммы оснований (средней линии) {self.get_half_sum()}"

    def get_half_sum(self) -> float:
        return (self.__up + self.__down) / 2
# !Trapeze

# int main() :)
if __name__ == "__main__":
    t = Trapeze(14, 16)
    print(t)
    pass