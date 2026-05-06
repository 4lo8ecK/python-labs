# Лабораторная работа №10
# Вариант 6
# Гаврилов Павел ФМ-11-25

import random as rnd    # для 'seed()' и 'randint()'
import time             # для 'time()' - для получения случайного seed'а

EXIT_CODES = ['exit', 'quit', 'close', 'q', 'й', 'учше', 'йгше', 'сдщыу', 'выход']

def clear_console() -> None:
    print('\033c', end='')
# !clear_console() -> None

def rand_list(
        elem_count: int = 10,
        _seed:      int = 0,
        min_value:  int = -10,
        max_value:  int = 10
        ) -> list:
# begin
    rnd.seed(_seed)
    return [rnd.randint(min_value, max_value) for _ in range(elem_count)]
# !rand_list(int, int, int, int) -> list

def rand_matrix(
        row:        int = 2,
        colomn:     int = 2,
        _seed:      int = 0,
        min_value:  int = -10,
        max_value:  int = 10
        ) -> list:
# begin 
    rnd.seed(_seed)
    res = []
    for i in range(row):
        res += [[rnd.randint(min_value, max_value) for _ in range(colomn)]]
    return res
# !rand_matrix(int, int, int, int, int) -> list

def rand_serial_list(
        elem_count:     int = 10,
        seed:           int = 0,
        min_value:      int = -10,
        max_value:      int = 10,
        max_series_len: int = 3
        ) -> list:
    rnd.seed(seed)
    tmp_series_values = rand_list(elem_count, seed, min_value, max_value)
    result = []
    for i in range(elem_count):
        for j in range(rnd.randint(1, max_series_len)):
            result += [tmp_series_values[i]]

    # удаление ссылок на уже ненужные объекты
    del result[elem_count:], tmp_series_values
    return result
# !rand_serial_list(int, int, int, int, int) -> list

def rand_serial_matrix(
        row:            int = 4,
        colomn:         int = 10,
        _seed:          int = 0,
        max_series_len: int = 5,
        min_value:      int = -10,
        max_value:      int = 10
        ) -> list:
    res = []
    for i in range(row):
        res += [rand_serial_list(colomn, _seed + i, min_value, max_value, max_series_len)]
    return res
# !rand_serial_matrix(int, int, int, int, int, int) -> list

def print_matrix(input: list) -> None:
    print('[', end='')
    for i in range(len(input)):
        endl = '\n'
        if i + 1 == len(input):
            endl = ''
        print(f"{input[i]}", end=endl)
    print(']')
# print_matrix() -> None

def task_1() -> None:
    seed = int(time.time() * 10000) % 100000
    mtx = rand_matrix(2, 10, seed)
    print("\tЗадание 1\n")
    print(f"Сид для генерации: {seed} - за основу взято время в unix-time")
    print(f"Случайная матрица в 2 строки и 10 столбцов\n\tx: {mtx[0]}\n\ty: {mtx[1]}\n")
    print("Номера столбцов, в которых представлены координаты точек I четверти:")
    print("\t(отсчёт начинается с 1)")

    count = 0

    for i in range(10):
        if mtx[0][i] > 0 and mtx[1][i] > 0:
            count += 1
            print(i + 1, end=' ')

    if count == 0: print("Нет таких точек")
    else: print(f"\nКоличество таких точек - {count}")
# !task_1() -> None

def task_2() -> None:
    seed = int(time.time() * 10000) % 100000
    arr = rand_serial_matrix(2, 10, seed, 5, 1, 10)
    
    print("\tЗадание 2\n")

    print(f"Сид для генерации: {seed} - за основу взято время в unix-time")
    print(f"Случайная матрица в 2 строки и 10 столбцов\n\tx: {arr[0]}\n\ty: {arr[1]}\n")

    t = arr[0][0] / arr[1][0]

    for i in range(1, 10):

        a = arr[0][i]
        b = arr[1][i]
        rel = a / b

        print(f"======= Колонна {i} =======\
              \n\tпервый элемент:\t{a}\n\tвторой элемент:\t{b}\n\tотношение:\t{rel}")
        if rel != t:
            print("\t=== не OK ===\n")
            break
        print("\t=== OK ===\n")
    # endloop
# !task_2() -> None

def task_3() -> None:
    print("\tЗадание 3\n")
    arr_len = input("Введите длину масива: ")
    if arr_len == '': arr_len = 5
    
    try:
        arr_len = int(arr_len)
    except ValueError:
        return
    
    seed = int(time.time() * 10000) % 10000
    x_arr = rand_list(arr_len, seed, -50, 50)
    a_arr = rand_matrix(arr_len, arr_len, seed, -50, 50)
    
    print(f"Сид для генерации: {seed} - за основу взято время в unix-time")
    print(f"\nСгенерированный массив X: {x_arr}\nСгенерированная матрица A:")
    print_matrix(a_arr)
    
    c_arr = []
    summ = 0
    for i in range(arr_len):
        for j in range(arr_len):
            summ += a_arr[i][j]
    
    for i in range(arr_len):
        if x_arr[i] < summ:
            c_arr += [summ]
        else:
            c_arr += [x_arr[i]]
    
    print(f"\nРезультат - С:\n{c_arr}")
    
# !task_3() -> None

def main():
    print("\tЛабораторная работа №10\n")
    print("Количество заданий - 3")
    print("Выберите задание:")
    cmd = input('→ ')
    if cmd in EXIT_CODES or cmd == '': exit(0)
    
    try:
        cmd = int(cmd)
    except ValueError:
        return

    while True:
        clear_console()
        if 1 <= cmd <= 3:
            match cmd:
                case 1: task_1()
                case 2: task_2()
                case 3: task_3()
        else:
            continue
        l_cmd = input('→ ')
        if l_cmd in EXIT_CODES: break
# !main() -> None

while True:
    clear_console()
    main()
    
