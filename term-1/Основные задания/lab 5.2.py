# Лабораторная работа №5
# Вариант 6
# Гаврилов Павел ФМ-11-25

# Задание 2
# Разработать программу для решения задачи определения места нахождения
# точки с произвольно заданными координатами на координатной плоскости. В случае
# если точка попадает в одну их выделенных областей (внутрь или на границу), про-
# грамма должна определять номер области или писать, что не попадает в нее. Границу
# области считать принадлежащей самой области и отдельно ее рассматривать не надо.
# При решении должны быть использованы условный оператор if.

import os

def clear_console():
    # если запускается на unix системах: macOS, linux
    if os.name == 'posix':
        os.system('clear')
    # если запускается на windows
    elif os.name == 'nt':
        os.system('cls')

# (x - a)**2 - (y - b)**2 = R**2

# True - внутри / на границе
# False - снаружи
def circle(x: float, y: float, a: float, b: float) -> bool:
    inside = ((x - a)**2 + (y - b)**2) <= 1
    if inside: return True
    else: return False
# !circle(float, float, float, float) -> bool

while True:
    clear_console()
    in_x = input()
    if in_x == 'exit':
        exit(0)
    in_y = input()

    try:
        in_x = float(in_x)
        in_y = float(in_y)
    except ValueError:
        print("Неверный ввод!")
        input()
        continue

    first = circle(in_x, in_y, 0, 1)    
    second = circle(in_x, in_y, 1, 0)    
    third = circle(in_x, in_y, 0, -1)    
    forth = circle(in_x, in_y, -1, 0)    
    fifth = circle(in_x, in_y, 0, 0)    

    M1: bool = ((-2 <= in_x < 0) and (0 < in_y <= 2)) and not(first and forth)
    M2: bool = ((1 <= in_x <= 2) and (0 <= in_y <= 2)) and not(first and second)
    M3: bool = ((0 <= in_y <= 1) and (0 <= in_x <= 1)) and (first and second and fifth)
    M4: bool = ((-1 <= in_y <= 1) and (-1 <= in_x <= 0)) and (fifth and not(third and forth))
    M5: bool = ((-2 <= in_y < 0) and (0 <= in_x <= 1)) and not(fifth and second)
    
    if in_x == 0.0 and in_y == 0.0:
        print("Точка в областях M3 и M4")
    elif M1:
        print("Точка в области M1")
    elif M2:
        print("Точка в области M2")
    elif M3:
        print("Точка в области M3")
    elif M4:
        print("Точка в области M4")
    elif M5:
        print("Точка в области M5")
    else:
        print("Точка вне любой из областей")

    if (input() == 'exit'): exit(0) 
