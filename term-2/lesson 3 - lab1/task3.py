import math as mt

class Complex:
    # конструктор класса
    def __init__(self, real: int|float = None, imag: int|float = 0) -> None:
        if real == None:
            raise ValueError("Необходимо ввести действительную часть числа")
        
        self.__real: int|float = real
        self.__imag: int|float = imag    
    
    # "деструктор" класса
    def __del__(self) -> None:
        del self.__real
        del self.__imag

    def __str__(self) -> str:
        return f"{self.__real} + {self.__imag}i"

    def mult(self, num: int|float|Complex) -> int|float|Complex:
        if isinstance(num, int) or isinstance(number, float):
            t_real = self.__real * num
            return t_real
        elif isinstance(num, Complex):
            t_real = (num.__real * self.__real) - (num.__imag * self.__imag)
            t_imag = 2 * (num.__imag * self.__imag)
            return Complex(t_real, t_imag)
    
    def get_arg(self):
        # 1-ая четверть
        angle = mt.degrees(mt.atan(abs(self.__imag / self.__real)))
        if self.__real > 0 and self.__imag > 0:
            return angle
        # 2-ая четверть
        if self.__real < 0 and self.__imag > 0:
            return 180 - angle
        # 3-я четверть
        if self.__real < 0 and self.__imag < 0:
            return -180 + angle
        # 4-ая четверть
        if self.__real > 0 and self.__imag < 0:
            return -1 * angle

# int main() :)
if __name__ == "__main__":
    cn1 = Complex(12, 2)
    cn2 = 2
    print(cn1.mult(cn2))
    print(cn1)
    print(Complex(cn2))
