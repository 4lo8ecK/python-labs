# Лабораторная работа №11
# Гаврилов Павел ФМ-11-25
# Вариант 6

import myui

def print_dict(inp: dict) -> None:
    keys = list(inp.keys())
    items = list(inp.values())

    for i in range(len(keys)):
        print(f"{keys[i]}: {items[i]}")
# !print_dict(dict) -> None

# Задание 1
_dict = {
    'судно 1': 'рыба',
    'судно 2': 'не рыба, а мясо',
    'судно 3': 'техника',
    'судно 4': 'футбольные мячи',
    'судно 5': 'бутсы',
    'судно 6': 'обычная обувь',
    'судно 7': 'всё подряд'}

def task_1() -> None:
    print("\tЗадание 1\n")
    print("Вывод словаря из 7 элементов")
    print("Все осальные задания так же работают с этим словарём")
    
    print("Ключ: значение")
    print_dict(_dict)
# !task_1() -> None

# Задание 2
def task_2() -> None:
    print("\tЗадание 2\n")
    print("Эта программа выводит список ключей")
    print("После чего выдаёт по запросу пользователя значение этого словаря по ключу")
    print("Необходимо ввести перечисленные ключи")
    print("Ключи: ")
    keys = list(_dict.keys())
    for i in keys:
        print(i)
    cmd = input("Ключ: ")
    print(_dict.get(cmd, "Нет такого варианта"))
# !task_2() -> None

def task_3() -> None:
    print('\tЗадание 3\n')
    print("Эта программа меняет местами ключи и значения словаря")
    
    keys = list(_dict.keys())
    items = list(_dict.values())

    res = {}
    for i in range(len(keys)):
        res[items[i]] = keys[i]
    
    print_dict(res)
# !task_3() -> None

functions_list = [task_1, task_2, task_3]
text_to_print = ['\n\tЛабораторная работа №11\n', 'Выберите задание']

myui.exec(functions_list, text_to_print)