# Дополнительное задание №1
# Вариант 6 
# Гаврилов Павел ФМ-11-25

import math
import myui as ui

#region TASK 1 
def func_t1(x: float = 0, a: float = 0) -> float:
    if x < 0:
        res = (a ** 2/3) - (x ** 2/3)
        if res < 0:
            return None
        return math.sqrt(res)
    
    else:
        if (a * 2 - x) == 0:
            return None
        res = (x ** 3) / (a * 2 - x)
        if res < 0:
            return None
        return a + math.sqrt(res)
# !func_t1(float, float) -> float

def task_1() -> None:

    print("\x1bc", end='')
    print("\x1b[2mДополнительное задание №2")
    print("Задание 1\x1b[0m")

    a = 0.8
    x = -a
    dx = round(a / 4, 1)

    print(f"a = {a}\ndx = {dx}")
    n = input("Введите x: ")
    if n == '': n = 12
    else: n = int(n)

    for i in range(n):
        res = func_t1(x=x, a=a)

        if res != None:
            res = round(res, 4)

        print(f"{i+1}\t\x1b[4Dres = {res}\tx = {x}")
        x = round(x + dx, 1)
    return
# !task_1() -> None
#endregion

#region TASK 2
def func_t2(k: float = 0) -> float:
    return k**3 + 25*(k**2) + 50*k + 1000

def task_2() -> None:
    print("\x1bc", end='')
    print("\x1b[2mДополнительное задание №2")
    print("Задание 2\x1b[0m")

    # константы
    A = 3 * (10 ** 4)
    B = 6 * (10 ** 4)
    M = 4
    T1 = math.sqrt(A * B * M)
    T2 = A + B + M

    rng_beg = -30
    rng_end = 60
    rng_count = 20
    rng_step: int = int((rng_end - rng_beg) // rng_count)

    print("\nЗначения функции \x1b[1m\x1b[3mf(K)\x1b[0m при \x1b[1m\x1b[3mK\x1b[0m")

    print('\x1b[2m', end='')
    print('-'*19)
    print('\x1b[0m', end='')

    print("   \x1b[3mK\t\x1b[2m|\x1b[0m результат")

    print('\x1b[2m', end='')
    print('-'*19)
    print('\x1b[0m', end='')

    count = 0
    for i in range(rng_beg, rng_end, rng_step):
        value = func_t2(i)
        if (value > 0) and (value < T1) and (value < T2):
            print(f"  {i}\t\x1b[2m|\x1b[0m  {value}\t")
        else:
            count += 1

    print('\x1b[2m', end='')
    print('-'*19)
    print('\x1b[0m', end='')

    print(f'количество исключений - {count}\n')
#endregion

#region TASK 3

def func_t3(x: float = 0, z: float = 0) -> float:
    if ((x**2 - z**2) < 0) or ((x+z) == 0): return None
    return round(((x-z)/(x+z))**2 + 2 * math.exp(math.sqrt(x**2 - z**2)) - (1/3), 3)


def task_3() -> None:
    print("\x1bc", end='')
    print("\x1b[2mДополнительное задание №2")
    print("Задание 3\x1b[0m")

    print('Введите значения')
    x0 = input('x0: ')
    hx = input('hx: ')
    n = input('n: ')

    z0 = input('z0: ')
    hz = input('hz: ')
    m = input('m: ')

    if x0 == '': x0 = 0
    if z0 == '': z0 = 0
    if hx == '': hx = 1
    if hz == '': hz = 1
    if n == '': n = 10
    if m == '': m = 10

    try:
        x0 = int(x0)
        z0 = int(z0)
        hx = int(hx)
        hz = int(hz)
        n = int(n)
        m = int(m)
    except ValueError:
        return

    tmp_x = x0
    tmp_z = z0
    for i in range(min(n, m)):
        print(f'при x = {tmp_x}, z = {tmp_z}: ', end='')
        for j in range(min(n, m)):
            res = func_t3(x=tmp_x, z=tmp_z)
            if res != None: print(f'{res}', end='\t')
            else: print(f' - ', end='\t')
            tmp_z += hz
        print('')
        tmp_z = z0
        tmp_x += hx

#endregion

#region UI

funcs = [task_1, task_2, task_3]
texts = [
    '\x1bc\n\tДополнительное задание №2',
    'Выберите задание'
]

ui.exec(funcs=funcs, txt=texts)
#endregion