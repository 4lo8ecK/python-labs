# Лабораторная работа №6
# Вариант 6
# Гаврилов Павел ФМ-11-25

# Задание 1
# Является ли заданное натуральное число степенью двойки?
import os

def clear_console():
    # если запускается на unix системах: macOS, linux
    if os.name == 'posix':
        os.system('clear')
    # если запускается на windows
    elif os.name == 'nt':
        os.system('cls')


def main():
    number = input()
    if number == 'exit':
        exit(0)

    try:
        number = int(number)
    except ValueError:
        print("Нужно ввести число")
    finally:
        for i in range(0,33):
            if number == 2 ** i:
                print(f"{number} является {i}-ой степенью двойки")
                break
        else:
            print(f"{number} не является степпенью двойки")
            

while(True):
    clear_console()
    main()
    if(input() == 'exit'):
        exit(0)