# Лабораторная работа №12
# Гаврилов Павел ФМ-11-25
# Вариант 6

import math
import myui

EXIT_CODES = ['exit', 'quit', 'close', 'q', 'й', 'учше', 'йгше', 'сдщыу', 'выход']

# Задание 1

def func_for_task_1(x: float = 1) -> float:
    res = (math.sqrt(1 + x ** 2) + (abs(math.log(x) ** 3) / (1.6 + x ** 4))) * math.sin(7 * x)
    return round(res, 5)
# !func_for_task_1(float) -> float

def task_1() -> None:
    print("\tЗадание 1\n")
    print("Программа выводит значение функции от x")
    print(f"Например, результат при x = 0.5: {func_for_task_1(0.5)}")
    inp_x = input("Введите x: ")

    if inp_x in EXIT_CODES: return

    try:
        inp_x = float(inp_x)
    except ValueError:
        return
    print(f"Резульат при x = {inp_x}: {func_for_task_1(inp_x)}")
# !task_1() -> None

def func_for_task_2(a: float = 1, b: float = 1, c: float = 1, power: float = 1) -> float:
    return ((1 + math.log(a) + c ** a)**3 +1 - b**3 + b**5) ** power
# !func_for_task_2(float, float, float, float) -> float

def task_2() -> None:
    print("\tЗадание 2\n")
    print("Программа выводит значение функции t")
    print(f"Например, результат при x = 5, a = 1, b = 1, c = 1, power = 1: {func_for_task_2(a=1, b=1, c=1, power=1)}")
    inp_x = input("Введите x: ")
    inp_a = input("Введите a: ")
    inp_b = input("Введите b: ")
    inp_c = input("Введите c: ")
    inp_power = input("Введите power: ")

    if inp_x in EXIT_CODES: return
    if inp_a in EXIT_CODES: return
    if inp_b in EXIT_CODES: return
    if inp_c in EXIT_CODES: return
    if inp_power in EXIT_CODES: return

    try:
        inp_a = float(inp_a)
        inp_b = float(inp_b)
        inp_c = float(inp_c)
        inp_power = float(inp_power)
    except ValueError:
        return
    print(f"Резульат:\n-> {func_for_task_2(a=inp_a, b=inp_b, c=inp_c, power=inp_power)}")
# !task_2() -> None

def func_for_task_3(x: float = 1, a: float = 1, b: float = 1) -> float:
    z = math.log(abs(b * (x**2)))
    res = None
    if x < a:
        res = 2.8 * math.sin(a * x - b * x**3 * z)
    elif a <= x <= b**2:
        res = z * math.cos(a * x + b)**2 + math.log(z)
    elif x > b**2:
        res = math.exp(2.5 * a * x) + z * a * b * x
    return res
# !func_for_task_2(float, float, float) -> float

def task_3() -> None:
    print("\tЗадание 3\n")
    print("Программа выводит значение функции от x")
    print(f"Например, результат при x = 5, a = 1, b = 1: {func_for_task_3(x=5 , a=1, b=1)}")
    inp_x = input("Введите x: ")
    inp_a = input("Введите a: ")
    inp_b = input("Введите b: ")

    if inp_x in EXIT_CODES: return
    if inp_a in EXIT_CODES: return
    if inp_b in EXIT_CODES: return

    try:
        inp_x = float(inp_x)
        inp_a = float(inp_a)
        inp_b = float(inp_b)
    except ValueError:
        return
    print(f"Резульат при\n\tx = {inp_x}\n\ta = {inp_a}\n\tb = {inp_b}:\n-> {func_for_task_3(x=inp_x, a=inp_a, b=inp_b)}")
# !task_3() -> None

def main():
    tasks_lst = [task_1, task_2, task_3]
    text_to_print = ['\n\tЛабораторная работа №12\n', 'Выберите задание']
    myui.exec(tasks_lst, text_to_print)

main()