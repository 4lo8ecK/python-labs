# Лабораторная работа №8
# Вариант 6
# Гаврилов Павел ФМ-11-25

# для генерации случайных списков
import random

# Очистка консоли (новый вариант через Backspace-последовательность)
def clear_console() -> None:
    print("\033c", end="")
# !clear_console() -> None

# Генерация списка размером в lst_len и со случайными значениями в диапазоне от 0 до lst_len
def rand_list(elem_count: int, seed: int = 0, min_value: int = -10, max_value: int = 10) -> list:
    random.seed(seed)
    return [random.randint(min_value, max_value) for _ in range(elem_count)]
# !rand_list(int, int) -> list

# Генерация списка с размером lst_len и со значениями от 0 до lst_len
def linear_list(elem_count: int) -> list:
    return [x for x in range(0, elem_count)]
# !linear_list(int) -> list

def rand_serial_list(elem_count: int, seed: int = 0, min_value: int = -10, max_value: int = 10, max_series_len: int = 3) -> list:
    random.seed(seed)
    tmp_series_values = rand_list(elem_count, seed, min_value, max_value)
    result = []
    for i in range(elem_count):
        for j in range(random.randint(1, max_series_len)):
            result += [tmp_series_values[i]]

    # удаление ссылок на уже ненужные объекты
    #del result[elem_count:len(result)], tmp_series_values
    del result[elem_count:], tmp_series_values
    return result

# Метод, меняющий местами элементы списка по их индексам
def swap_list_elements(lst: list, first: int, second: int) -> None:
    lst[first], lst[second] = lst[second], lst[first]
# !swap_list_elements(list, int, int) -> None

# Методы заданий

# Задание 1
def task_1() -> None:
    print("Задание 1")
    print("Программа выдаёт максимально приближенный к введённому числу элемент массива")
    
    r = input("Искомое число: ")
    if r == '': return
    if r == 'exit': exit(0)

    lst_len = input("Размер массива: ")
    if lst_len == '' or lst_len == 'exit': return
    
    try:
        r = int(r)
        lst_len = int(lst_len)
    except ValueError:
        print("Нужно ввести числа!")
        input("Нажмите [Enter]")
        return
    
    lst = rand_list(lst_len, 0)
    print("Массив чисел:\n->",lst)

    min_delta = lst_len
    number = 0

    for i in range(0, lst_len):
        local_delta = abs(lst[i] - r)
        if local_delta < min_delta:
            min_delta = local_delta
            number = lst[i]
    
    print(f"Максимально приближенное к {r} число - {number}")
# !task_1() -> None

# Задание 2
def task_2() -> None:
    print("Задание 2")
    print("Программа выдаёт изначальный массив случайных чисел")
    print("А после удаляет из него элементы с нечётным индексом и выводит полученный список")
    print("Размер списка - не менее 2-ух элементов")

    lst_len = input("Введите размер массива: ")
    if lst_len == '': return
    if lst_len == 'exit': exit(0)

    try:
        lst_len = int(lst_len)
    except ValueError:
        print("Нужно ввести числа!")
        input("Нажмите [Enter]")
        return

    if lst_len < 2: return

    lst1 = rand_list(lst_len, 1)
    print(f"Полученный случайным образом массив:\n-> {lst1}")
    
    lst = []
    for i in range(0, lst_len, 2):
        lst += [lst1[i]]
    del lst1
    
    print(f"Итоговый массив:\n-> {lst}")
# !task_2() -> None

# Задание 3
def task_3() -> None:
    print("Задание 3")
    print("Программа выдаёт изначальный массив случайных точек с координатами x, y")
    print("Потом сортирует их по принципу (x1,y1) < (x2,y2), если:")
    print("\tx1 < x2 или x1 = x2 и y1 < y2")

    points_count = input("\nВведите размер списка: ")
    if points_count == '': return
    if points_count == 'exit': exit(0)
    
    try:
        points_count = int(points_count)

    except ValueError:
        print("Нужно ввести целочисленные значения!")
        return
    except:
        print("Представления не имею, что пошло не так...")
        return

    lst = []
    for i in range(0, points_count):
        lst += [rand_list(2, i)]
    print(f"Изначальный список:\n{lst}")

    # Пузырьковая сортировка :)
    for i in range(0, len(lst)):
        for j in range(i + 1, len(lst)):
            if (lst[i][0] > lst[j][0]) or (lst[i][0] == lst[j][0] and lst[i][1] > lst[j][1]):
                swap_list_elements(lst, i, j)

    print(f"\nПолученный в итоге список:\n{lst}")
# !task_3() -> None

def task_4() -> None:

    print("Задание 4")
    print("Эта программа удаляет определённую серию из списка")
    print('''Серией назовем группу подряд идущих одинаковых элементов, а длиной серии –
    количество этих элементов (длина серии может быть равна 1).''')
    print("Отсчёт номера серии начинается с 1")
    print("")

    lst_len = input("Введите размер списка: ")
    if lst_len == 'exit' or lst_len == '': return

    try:
        lst_len = int(lst_len)
        lst = rand_serial_list(lst_len)
        print(f"Cписок:\n{lst}")
        series = []
        tmp = [lst[0]]

        for i in range(1, len(lst)):
            if lst[i] == lst[i - 1]:
                tmp.append(lst[i])
            else:
                series.append(tmp)
                tmp = [lst[i]]
        series.append(tmp)
        del tmp, lst
        print(f"Список, разделённый на серии:\n{series}\n")

        series_to_delete = input("Введите номер серии для удаления: ")
        if series_to_delete == 'exit' or series_to_delete == '': return
        series_to_delete = int(series_to_delete)
        
    except ValueError:
        print("Нужно ввести целочисленные значения!")
        return
    except:
        print("Представления не имею, что пошло не так...")

    if series_to_delete < 1:
        print("Значение номера серии для удаления должно быть больше 1")
        return

    if series_to_delete <= len(series):
        # т.к. номер серии, введённый пользователем != номер серии в списке
        # ведь предполагается, что пользователь начинает отсчёт с 1, а не с 0 
        del series[series_to_delete - 1]
        print(f"Список с удалённой серией №{series_to_delete}:\n{series}")

    else:
        print(f"Введённый номер серии на удаление был больше количества серий данного списка")

def main() -> None:
    clear_console()
    print("Лабораторная работа №8")
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