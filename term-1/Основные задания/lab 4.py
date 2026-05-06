# Лабораторная работа №4
# Вариант 6
# Гаврилов Павел ФМ-11-25
# Код к каждому заданию как для отдельной программы

print("# Лабораторная работа №4\nВариант 6\nГаврилов Павел ФМ 11-25\nКод к каждому заданию как для отдельной программы\n")

import math

# Задание 1
print("\nЗадание 1")

print("Введите число: ", end='')
x = float(input())
print("Результат = ",end='')
if x < -1:
    print(0)
elif -1 <= x < 0:
    print(1)
elif 0 <= x < 2:
    print(-1)
elif x >= 2:
    print(1)


# Задание 2
"""
Задание 2 Написать программу вычисления значения функции у(х) для всех различных
вариантов входных параметров. Ввести с клавиатуры х. Значения всех неизвестных вве-
сти с клавиатуры. Значения переменных, которые вычисляются, с клавиатуры не вво-
дятся. Вывести значение функции. При вводе значений обязательны поясняющие
надписи! (в input()). При выводе значения тоже сделать поясняющие подписи (в print).
"""
print("\nЗадание 2")

print("Введите x: ", end='')
x = float(input())

print("Введите a: ", end='')
a = float(input())

print("Введите b: ", end='')
b = float(input())

print("Введите c: ", end='')
c = float(input())

res = None
if math.exp(a + b) < math.exp(x):
    res = math.sin(math.exp(a + b)) + (x ** 2)

elif math.exp(a + b) == math.exp(x):
    res = math.atan(a * b * c) + (x ** (1/3))

elif math.exp(a + b) > math.exp(x):
    res = math.cos(math.sqrt(abs(x + (a * b * c))))

print(f"Результат вычислений: {res}")

# Задание 3
"""
Задание 3 Вычислить значение функции в точке x. Значение x ввести с клавиатуры.
Точку разрыва обработать отдельно. В тетради расписать все функции!
"""

print("\nЗадание 3")
print("Это программа выдаёт значения функции по оси OY")
print("Введите значение по OX в диапазоне от -9 до 9 включительно")

def get_circle_y(input_x, circle_x, circle_y, circle_rad) -> float:
    return -1 * (math.sqrt(abs((circle_rad ** 2) - ((input_x - circle_x) ** 2 ))) - circle_y)
# используется abs(), т.к. при некоторых значениях input_x подкоренное выражение МЕНЬШЕ нуля.
# например, такое было с числом приблизительно равным 7.90000
# get_circle_y

def get_line_y(x, k, b) -> float:
    return k * x + b
# get_line_y

print("x = ", end='')
x = float(input())

def calculate(x):
    res = None
    if -9 <= x <= 9:
        if -9 <= x < -7:
            res = get_circle_y(x, -9, -5, 1)
        elif -8 <= x < -7:
            res = get_circle_y(x, -8, -4, 1)
        elif -7 <= x < -2:
            res = get_line_y(x, -0.6, -8.2)
        elif -2 <= x < 3:
            res = get_line_y(x, 1.8, -3.4)
        elif 3 <= x < 6:
            res = get_line_y(x, (-1/3), 3)
        elif 6 <= x < 7:
            res = get_circle_y(x, 6, 2, 1)
        elif 7 <= x <= 9:
            res = get_circle_y(x, 9, 2, 2)

    else:
        print("Число вне дипазона от -9 до 9")
        exit(0)

    return res

print(f"При x = {round(x, 4)}, y = {round(calculate(x), 4)}")

# тест
# проверка значений в заданном диапазоне с шагом в 0.1
"""
i = -9.0    
while i <= 9.0:
    print(f"При x = {round(i, 4)}, y = {round(calculate(i), 4)}")
    i += 0.1

"""