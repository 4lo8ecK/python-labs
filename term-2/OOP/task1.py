import math as m

class Triangle:
    # из прошлого занаятия
    def __init__(self, a, b, c):
        if a <= 0 and b <= 0 and c <= 0:
            raise ValueError('<0')
        if a+b<=c or b+c<=a or c+a<=b:
            raise ValueError('no tr')
        sides = sorted([a,b,c])
        self.a, self.b, self.c = sides

    def __str__(self):
        return f'{self.a},{self.b},{self.c}'

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter()/2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5

    def is_equilateral(self, eps=0.0001):
        return abs(self.a-self.b)<=eps and abs(self.b-self.c)<=eps
        
    # задание 1

    # возвращает 
    def angles(self) -> tuple[float]:
        alpha: float = m.acos((self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c))
        beta: float = m.acos((self.b**2 + self.a**2 - self.c**2) / (2 * self.b * self.a))
        gamma: float = m.acos((self.a**2 + self.c**2 - self.b**2) / (2 * self.c * self.a))
        return (alpha, beta, gamma)

    def is_isoscele(self) -> bool:
        if self.a == self.b or self.a == self.c or self.b == self.c:
            return True
        return False
    pass

