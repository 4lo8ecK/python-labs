# Лабораторная работа №6
# Вариант 6
# Гаврилов Павел ФМ-11-25

# Задание 3

import os

def clear_console():
    # если запускается на unix системах: macOS, linux
    if os.name == 'posix':
        os.system('clear')
    # если запускается на windows
    elif os.name == 'nt':
        os.system('cls')

b1 = 0

def main():
    num = input('Введите число больше нуля: ')
    if num == 'exit' or num == '': exit(0)

    try:
        num = int(num)

    except ValueError:
        print('Нужно ввести число!')

    else:

        print(f"Первые {num} элементов последовательности:\n-> ", end='')

        if num > 0:
            prev_value = b1
            print(b1, end=' ')

            for i in range(1, num):
                res = 0
                if i % 2 == 0:
                    res = prev_value + 3
                    prev_value = res
                else:
                    res = 2 * (prev_value + 3)
                    prev_value = res

                print(res, end=' ')
        
        else:
            print("Число должно быть больше нуля!")
while True:
    clear_console()
    main()
    cmd = input('\n')
    if cmd == 'exit': exit(0)