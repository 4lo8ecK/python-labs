import math as m

class Triangle:
    # из прошлого занаятия
    def __init__(self, a: int|float, b: int|float, c: int|float) -> None:
        if a <= 0 and b <= 0 and c <= 0:
            raise ValueError('<0')
        if a+b<=c or b+c<=a or c+a<=b:
            raise ValueError('no tr')
        sides = sorted([a,b,c])
        self.a, self.b, self.c = sides

    def __str__(self) -> str:
        return f'{self.a},{self.b},{self.c}'

    # периметр
    def perimeter(self) -> float:
        return self.a + self.b + self.c

    # площадь
    def area(self) -> float:
        p = self.perimeter()/2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5

    # является ли равносторонним
    def is_equilateral(self, eps=0.0001) -> bool:
        return abs(self.a-self.b)<=eps and abs(self.b-self.c)<=eps
        
    # задание 1
    # возвращает кортеж из углов
    def angles(self) -> tuple[float]:
        alpha: float = m.acos((self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c))
        beta: float = m.acos((self.b**2 + self.a**2 - self.c**2) / (2 * self.b * self.a))
        gamma: float = m.acos((self.a**2 + self.c**2 - self.b**2) / (2 * self.c * self.a))
        return (alpha, beta, gamma)

    # является ли равнобедренным
    def is_isoscele(self) -> bool:
        if self.a == self.b or self.a == self.c or self.b == self.c:
            return True
        return False
    
    # является ли прямоугольным
    def is_right(self) -> bool:
        ra = round(self.a, 9)
        rb = round(self.b, 9)
        rc = round(self.c, 9)
        if (ra**2 + rb**2) == rc**2: return True
        elif (rb**2 + rc**2) == ra**2: return True
        elif (ra**2 + rc**2) == rb**2: return True
        return False

    # является ли острым
    def is_acute(self) -> bool:
        if self.a < (self.b**2 + self.c**2): return True 
        elif self.b < (self.a**2 + self.c**2): return True 
        elif self.c < (self.a**2 + self.b**2): return True 
        return False
    
    # является ли тупым
    def is_obtuse(self) -> bool:
        if self.a > (self.b**2 + self.c**2): return True 
        elif self.b > (self.a**2 + self.c**2): return True 
        elif self.c > (self.a**2 + self.b**2): return True 
        return False

    def triangel_type(self) -> str:
        angles: tuple[float] = self.angles()
        a_type = ''
        if self.is_equilateral():
            a_type = 'равносторонний'
        else:
            if self.is_right():
                a_type = 'прямоугольный'
            elif self.is_acute():
                a_type = 'острый'
            elif self.is_obtuse():
                a_type = 'тупой'
        s_type = ''
        if self.is_isoscele():
            s_type = ', равнобедренный'
        ang = self.angles()
        return f'Углы {ang[0], ang[1], ang[2]}, {a_type}{s_type}'

t = Triangle(3,4,4)
print(t)
print(t.triangel_type())