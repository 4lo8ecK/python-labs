# Лабораторная работа №7
# Вариант 6
# Гаврилов Павел ФМ-11-25

import os

def clear_console():
    # если запускается на unix системах: macOS, linux
    if os.name == 'posix':
        os.system('clear')
    # если запускается на windows
    elif os.name == 'nt':
        os.system('cls')

# Задание 1
def task_1():
    clear_console()
    print("Задание 1")
    print("Возвращает буквосочетание из 2 и 4 символа введённого текста")
    input_string = input("Введите слово длиной более 4 символов: ")
    if len(input_string) < 4:
        print("Слово должно быть более 4 символов!")
        return False
    print(input_string[1] + input_string[3])
    return True
# Задание 2
def task_2():
    clear_console()
    print("Задание 2")
    print("Выдаёт количество букв 'н' и 'м'")
    input_string = input("Введите любой текст: ")

    n_count = input_string.count('н')
    m_count = input_string.count('м')
    n_big_count = input_string.count('Н')
    m_big_count = input_string.count('М')

    # ТУПОЙ ВАРИАНТ РЕШЕНИЯ!!!
    '''
    n_count = 0
    m_count = 0
    n_big_count = 0
    m_big_count = 0

    for i in range(0, len(input_string)):
        if input_string[i] == 'н':
            n_count += 1
        elif input_string[i] == 'м':
            m_count += 1
        elif input_string[i] == 'Н':
            n_big_count += 1
        elif input_string[i] == 'М':
            m_big_count += 1
    '''
    print("Результат:")
    if n_count > 0 or n_big_count > 0:
        print(f"кол-во букв 'н' всего - {n_count + n_big_count}:\n\t{n_count} строчных\n\t{n_big_count} прописных")

    if m_count > 0 or m_big_count > 0:
        print(f"кол-во букв 'м' всего - {m_count + m_big_count}:\n\t{m_count} строчных\n\t{m_big_count} прописных")
    else:
        print("Нет букв 'н' и 'м'")

# Задание 3
def task_3():
    clear_console()
    print("Задание 3")
    print("Возвращает количество прописных латинских символов")

    input_string = input("Ввод: ")
    big_sym_count = 0
    for i in range(0, len(input_string)):
        if ord(input_string[i]) in range(65, 91):
            big_sym_count += 1

    print(f"Ответ - {big_sym_count}")

# Задание 4
def task_4():
    clear_console()
    input_string = input("Введите строку: ")
    number = input("Введите число: ")
    if number.isnumeric():
        number = int(number)
    else:
        return False

    if len(input_string) > number:
        print(input_string[(len(input_string) - number)::])
    elif len(input_string) < number:
        print( str('.' * (number - len(input_string))) + str(input_string))

# Задание 5
def task_5():
    clear_console()
    print("Задание 7")
    print("Смещение символов определённого промежутка в право на один")
    word = input("Введите само слово/текст:\n-> ")
    s = input("Верхняя граница: ")
    k = input("Нижняя граница: ")
    if k.isnumeric() and s.isnumeric():
        k = int(k)
        s = int(s)
    else:
        print("Границы должны определяться числами")
        return False

    if not(0 <= s <= len(word)) or not(0 <= k <= len(word)):
        print("Промежуток выходит за пределы границ слова")
        return False
    if s <= k:
        print("Верхняя граница не может быть меньше нижней")
        return False

    res = list(word)
    for i in range(k-1, s):
        res[i] = word[i - 1]
    res[k-1] = word[s-1]
    
    res = str(''.join(str(x) for x in res))
    print(res)
    return True

def main():
    clear_console()
    print("Лабораторная работа №7")
    print("Выберите задание от 1 до 5")
    cmd = input()
    if cmd == 'exit' or cmd == '':
        exit(0)
    if not cmd.isnumeric():
        print("Команда должна быть числом")
    else:
        cmd = int(cmd)
        if 1 <= cmd <= 5:
            match cmd:
                case 1: task_1()
                case 2: task_2()
                case 3: task_3()
                case 4: task_4()
                case 5: task_5()
        else:
            print("Неизвестная команда")

while True:
    main()
    cmd = input()
    if (cmd == 'exit'): exit(0)