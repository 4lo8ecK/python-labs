# Лабораторная работа №6
# Вариант 6
# Гаврилов Павел ФМ-11-25

# Задание 2
# Дано целое число n (>0). Найти двойной факториал n:
# n!! = n*(N—2)*(N—4)*...
# (последний сомножитель равен 2, если n – четное, и 1, если n – нечетное).
# Чтобы избежать целочисленного переполнения, вычислять это произведе-
# ние с помощью вещественной переменной и вывести его как вещественное
# число.

import os

def clear_console():
    # если запускается на unix системах: macOS, linux
    if os.name == 'posix':
        os.system('clear')
    # если запускается на windows
    elif os.name == 'nt':
        os.system('cls')

def main():
    n = input("Введите число: ")
    if n == 'exit' or n == '': exit(0)

    try:
        n = int(n)

    except ValueError:
        print("Нужно ввести число")

    finally:
        x = 1
        if n % 2 == 0:
            x = 2
        else:
            x = 1
        if n >= 1:
            on_step = n - 2
            res = n
            while on_step >= x:
                res *= on_step
                on_step -= 2
            print(f"Двойной факториал числа {n} = {res}")
        else:
            print("Число должно быть больше 0!")

while True:
    clear_console()
    main()
    if input() == 'exit': exit(0)