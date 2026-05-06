# Лабораторная работа №5
# Вариант 6
# Гаврилов Павел ФМ-11-25

# Задание 1
# С клавиатуры задается точка M c координатами x и y. Определить, попадает
# ли точка с заданными координатами в область, закрашенную на рисунке серым
# цветом, лежит на границе этой области или не попадает в эту область. Результат
# работы программы вывести в виде текстового сообщения.
# В тетради расписать все функции!

import os

def clear_console():
    # если запускается на unix системах: macOS, linux
    if os.name == 'posix':
        os.system('clear')
    # если запускается на windows
    elif os.name == 'nt':
        os.system('cls')

# 0 - внутри фигуры
# 1 - на границе
# 2 - вне фигуры
# 3 - чудо
def tris(x: float, y: float, b1: float, b2: float, y0: float, x1: float, x2: float) -> int:
    inside = ((y > y0) and (y < x + b1) and (y < -1 * x + b2)) and (x > 0 and y > 0)
    outside = (y < y0) or (y > x + b1) or ( y > -1 * x + b2)
    bound = ((y == y0) or (y == x + b1) or ( y == -1 * x + b2)) and (x1 <= x <= x2) and (x > 0 and y > 0)
    if inside:
        return 0
    elif bound and not(outside):
        return 1
    elif outside:
        return 2
    else:
        return 3
# tris(float, float, float, float) -> float

# 1st: y = 0, y = x, y = -x + 6
# 2nd: y = 3, y = x + 2, y = -x + 8
# 3rd: y = 5, y = x + 3, y = -x + 9

def main():
    input_x = input('Введите x: ')
    input_y = input('Введите y: ')

    try:
        input_x = float(input_x)
        input_y = float(input_y)
    except ValueError:
        exit(0)
    
    first = tris(input_x, input_y, 0, 6, 0, 0, 6)
    second = tris(input_x, input_y, 2, 8, 3, 1, 5)
    third = tris(input_x, input_y, 3, 9, 5, 2, 4)

    if (first == 0) or (second == 0) or (third == 0):
        print("Внутри фигуры")
    elif (first == 1) or (second == 1) or (third == 1):
        print("На границе фигуры")
    elif (first == 2) or (second == 2) or (third == 2):
        print("Вне фигуры")
    else:
        print("Не имею представления, как до этого дошло")

while True:
    clear_console()
    main()
    x = input()
    if (x == 'exit'):
        exit(0)