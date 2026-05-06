# Дополнительное задание №1
# Вариант 6 
# Гаврилов Павел ФМ-11-25

import random as rnd    # для 'seed()' и 'randint()'
import time             # для 'time()' - для получения случайного seed'а

EXIT_CODES = ['exit', 'quit', 'close', 'q', 'й', 'учше', 'йгше', 'сдщыу', 'выход']

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

def print_matrix(input: list) -> None:
    for i in range(len(input)):
        endl = '\n'
        if i + 1 == len(input):
            endl = ''
        print(f"{input[i]}", end=endl)
    print()
# !print_matrix(list) -> None

def mirror_matrix(mtx: list) -> None:
    for i in mtx:
        i.reverse()
# !mirror_matrix(list) -> None

def diagonals_of_mtx(mtx: list) -> list:
    result = []
    length = len(mtx)
    mirror_matrix(mtx)
    for i in range(2 * length - 1):
        tmp_diagonal = []
        row = 0
        colomn = 0

        if i < length:
            row = 0
            colomn = i
        
        else:
            row = i - length + 1
            colomn = length - 1
            
        while row < length and colomn >= 0:
            tmp_diagonal += [mtx[row][colomn]]
            row += 1
            colomn -= 1
        
        result += [tmp_diagonal]
    mirror_matrix(mtx)
    return result
# !diagonals_of_mtx(list) -> list

def get_lower_part(d: int, diagonals: list) -> list:
    res = []
    for i in range(d, len(diagonals)):
        for j in diagonals[i]:
           res += [j] 
    return res
# !get_lower_part(list) -> list

def main():
    seed = int(time.time() * 10000) % 100000

    print("\tДополнительное задание №1\n")
    print(f"Сид для генерации: {seed} - за основу взято время в unix-time")

    d = input("Введите размеры матрицы: ")
    if d in EXIT_CODES: return
    if d == '': d = 4

    try:
        d = int(d)
    except ValueError:
        return
    print(f"d = {d}\n")
    mtx = rand_matrix(row=d, colomn=d, _seed=seed, min_value=-10, max_value=10)
    
    print("=== Полученная матрица ===")
    print_matrix(mtx)
    print()

    diagonals = diagonals_of_mtx(mtx)
    lower_part = get_lower_part(d, diagonals)

    res = None
    is_found = False

    count = 0
    while not is_found:
        for i in lower_part:
            if i <= 0:
                res = i
                is_found = True
                break
        else:
            for i in range(len(lower_part)):
                lower_part[i] *= 3

        if count == 50:
            is_found = True
        count+=1
    # endloop
    print(f"Результат: {res}")

while True:
    print('\033c', end='') # очистка консоли
    main()
    if input("-> ") in EXIT_CODES: exit(0)