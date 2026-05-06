# Лабораторная работа №9
# Вариант 6
# Гаврилов Павел ФМ-11-25

# для генерации случайных списков
from random import seed, randint
from math import sqrt

# Очистка консоли (новый вариант через Backspace-последовательность)
def clear_console() -> None:
    print("\033c", end="")
# !clear_console() -> None

# Генерация списка размером в lst_len и со случайными значениями в диапазоне от 0 до lst_len
def rand_list(elem_count: int, _seed: int = 0, min_value: int = -10, max_value: int = 10) -> list:
    seed(_seed)
    return [randint(min_value, max_value) for _ in range(elem_count)]
# !rand_list(int, int) -> list

def task_1() -> None:
    print("Задание 1")
    print("Программа выводит сумму элементов массива с индексами квадратов натуральных чисел")
    print("и меньше квадратного корня длины массива\n")

    arr_len = input("Введите длину массива для генерации: ")
    if arr_len == '': return
    if arr_len == 'exit': exit(0)

    try:
        arr_len = int(arr_len)
    except ValueError:
        print("Нужно ввести число!")
        input("Нажмите [Enter]")
        return

    arr = rand_list(arr_len, 0, 0, 100)
    arr_len_sqrt = sqrt(arr_len)

    print(arr)
    res = 0
    for i in range(0, arr_len):
        sq_i = i ** 2
        if sq_i < arr_len_sqrt:
            res += arr[sq_i]

    print(res)
# !task_1() -> None

def task_2() -> None:
    print("Задание 2")
    arr_len = input("Введите длину массива: ")
    if arr_len == 'exit': exit(0)
    if arr_len == '': return

    w = input("Введите число W: ")
    if w == 'exit': exit(0)
    if w == '': return

    try:
        arr_len = int(arr_len)
        w = int(w)
    
    except ValueError:
        print("Нужно ввести число!")
        input("Нажмите [Enter]")
        return

    arr = rand_list(arr_len, 1, -100, 100)

    print(arr)

    m1 = 0
    m2 = 0
    c1 = 0
    c2 = 0

    for i in arr:
        if i > w:
            c1 += i
            m1 += 1
        elif i < -w:
            c2 += i
            m2 += 1
    
    print("\nc1 - сумма элементов списка, которые больше w, m1 - количество таких элементов")
    print("c2 - сумма элементов списка, которые меньше -w, m2 - количество таких элементов")
    print(f"\nc1 = {c1}\nm1 = {m1}")
    print(f"c2 = {c2}\nm2 = {m2}")
# !task_2() -> None

def task_3() -> None:
    print("Задание 3")
    print("Эта программа выводит произведение наибольшего элемента из первого массива и наименьшего из второго")
    arr_len = input("Введите длину массива: ")

    if arr_len == '': return
    if arr_len == 'exit': exit(0)

    try:
        arr_len = int(arr_len)

    except ValueError:
        print("Нужно ввести число!")
        input("Нажмите [Enter]")
        return
    
    arr_a = rand_list(arr_len, 1, -100, 100)
    arr_c = rand_list(arr_len, 2, -100, 100)

    print(f"Первый массив:\n-> {arr_a}")
    print(f"Второй массив:\n-> {arr_c}")
    
    print("\nРезультат:\n-> ",max(arr_a) * min(arr_c))
# !task_3() -> None

def task_4() -> None:
    arr_len = input("Введите длину массива: ")
    if arr_len == 'exit': exit(0)
    if arr_len == '': return
    try:
        arr_len = int(arr_len)
    except ValueError:
        print("Нужно ввести число!")
        input("Нажмите [Enter]")
        return
    
    arr = rand_list(arr_len)
    print(f"Массив чисел:\n-> {arr}")
    for i in range(0, arr_len):
        if abs(arr[i]) % 2 == 0:
            print(f"Чётный элемент {arr[i]}, его индекс - {i}")
# !task_4() -> None

def main() -> None:
    clear_console()
    print("Лабораторная работа №9")
    print("Количество заданий - 4")
    print("Выберите задание от 1 до 4")

    cmd = input(": ")
    if cmd == 'exit' or cmd == '':
        exit(0)
    if not cmd.isnumeric():
        print("Команда должна быть числом")
    else:
        clear_console()
        cmd = int(cmd)
        if 1 <= cmd <= 5:
            match cmd:
                case 1: task_1()
                case 2: task_2()
                case 3: task_3()
                case 4: task_4()
        else:
            print("Неизвестная команда")

while True:
    main()
    cmd = input()
    if (cmd == 'exit'): exit(0)