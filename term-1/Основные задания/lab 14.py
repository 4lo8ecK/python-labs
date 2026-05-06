# Лабораторная работа №13
# Вариант 6
# Гаврилов Павел ФМ-11-25

import os
import textedit as txt
import myui as ui

# Названия директорий
LAB_DIR_PATH = 'lab14-files'
CONST_DIR_NAME = 'const-files'

# Названия файлов для
TASK_1 = 'task1.txt'
TASK_2 = 'task2.txt'

#region INIT
def create_file(path: str = "untitled.txt", data: str = "") -> bool:
    try:
        with open(file=path, mode='w', encoding='utf-8') as file:
            file.write(data)
    except PermissionError:
        print(f'\x1bcНедостаточно прав для редактирования {path}')
        return False
    except Exception as e:
        print(f'\x1bcКод исключения:\n{e}')
        return False
    return True

# Инициализация программы
# Создаёт нужные файлы, считав текст из 'const files'
def init_prog() -> None:
    if not os.path.exists(LAB_DIR_PATH):    # проверка на наличие нужной директории для файлов
        os.mkdir(LAB_DIR_PATH)
    if not os.path.exists(CONST_DIR_NAME):
        print('\x1bcНе удалось найти директорию "const-files"\nСоздайте её вручную в той же директории, что и исполняемый файл')
        exit(3)

    # Отрывок из 27 главы романа М. Булгакова 'Мастер и Маргарита'
    # Сцена ареста простого чёрного кота, чинящего примус
    master_and_margarita: str = ''
    try:
        with open(file=(os.path.join(CONST_DIR_NAME,'lab14.txt')), mode='r', encoding='utf-8') as const_file:
            master_and_margarita = txt.normalize(const_file.read(), '')
            # `txt.normalize(str, str) -> str` - удаляет лишние пробелы из текста
    except FileNotFoundError:
        print('\x1bcНе удалось найти файл "lab14.txt" в директории "const-files". Для работы программы создайте этот файли и напишите в нём хотя бы 2 строки абсолютно любого текста')
        exit(3)
    except Exception as e:
        print(f'\x1bcКод исключения:\n{e}')
        exit(3)

    # Создание файла для 1-го задания
    if not create_file(path=os.path.join(LAB_DIR_PATH, TASK_1), data=master_and_margarita):
        print('\x1bcОшибка создания файла {TASK_1}')
        exit(3)

    # Создание файла для 2-го задания
    paragraphs = txt.getlines(master_and_margarita)
    for line in paragraphs:
        line = str(' ' * 5) + line
    res = txt.normalize(paragraphs, '\n')
    if not create_file(path=os.path.join(LAB_DIR_PATH, TASK_2), data=res):
        print('\x1bcОшибка создания файла {TASK_1}')
        exit(3)
    return
#endregion

#region TASKS
def task_1() -> None:
    print('\x1bc\n\tЛабораторная работа №14')
    print('Задание 1')
    print('Нужно вставить строку S в начало файла')
    
    s = input('Строка для записи: ')
    with open(file=os.path.join(LAB_DIR_PATH,TASK_1), mode='r+', encoding='utf-8') as file:
        tmp_dat = file.read()
        file.seek(0)
        file.write(s + '\n' + tmp_dat)
        del tmp_dat
    return None

def task_2() -> None:
    print('\x1bc\n\tЛабораторная работа №14')
    print('Задание 2')
    print('Нужно добавить пустые строки между абзацами')

    with open(file=os.path.join(LAB_DIR_PATH, TASK_2), mode='r+', encoding='utf-8') as file:
        lines = file.readlines()
        file.seek(0)
        file.write(txt.normalize(lines, '\n'))
        del lines
    return None 
#endregion

#region UI_LOGIC
funcs = [task_1, task_2]
texts = [
    '\x1bc\n\tЛабораторная работа №14',
    'Выберите задание'
]

init_prog()
ui.exec(funcs=funcs, txt=texts)
#endregion
