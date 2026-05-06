# Лабораторная работа №3
# Вариант 6
# Гаврилов Павел ФМ-11-25

def end_program():
    print("\n\t\tПрограмма завершена")
    print("\t-- Нажмите на [Enter] для выхода --")
    input()
    exit()
# end_program

# Задание 1

print("\tЛабораторная работа №3")
print("\tВариант 6\n")
print("Задание 1")
print("Эта программа проверяет, может ли первый прямоугольник уместиться внутри вторго")

print("Введите стороны первого прямоугольника:")
print("a: ", end='')
a = input()
print("b: ", end='')
b = input()
print("\nВведите стороны второго прямоугольника:")
print("c: ", end='')
c = input()
print("d: ", end='')
d = input()

try:
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)

except ValueError:
    print("Необходимо ввести числа!")
    end_program()

if (a < c) and (b < d):
    print("Может:\nПервый прямоугольник помещается внутри второго")
else:
    print("Не может:\nПервый прямоугольник НЕ помещается внутри второго")

print("\n\t--- Конец первой программы ---\n")

# Задание 2

# Необходимо выяснить, может ли белая фигура (ферзь или ладья)
# попасть под удар если пойдёт на (x1;y1),
# когда чёрная фигура (ферзь или ладья) стоит на (x2;y2)

# также есть "первоначальное положение" белой фигуры -> 
#       -> нужно проверить возможность такого хода

# максимальное значение координаты по оси - 8
# минимальное - 1

# подразумевается, что пользователь сам выбирает, какая фигура - ферьзь, а какая - ладья
# для этого будет использоваться bool:
#   True    - ферзь
#   False   - ладья

"""
from time import sleep  # подключён для паузы при неверном вводе пользователя,
                        # после отсчёта 3-х секунд будет завершена сама программа
"""

def horizontal_move(init_y: int, mov_y: int) -> bool:
    return (init_y == mov_y)

def verical_move(init_x: int, mov_x: int) -> bool:
    return (init_x == mov_x)

def diagonal_move(init_x: int, init_y: int, mov_x: int, mov_y: int) -> bool:
    _a = abs(init_x - mov_x)
    _b = abs(init_y - mov_y)
    return (_a == _b)

# проверяет возможность хода фигуры
# то есть, применим и для проверки существования хода белой фигуры,
# и для проверки того, может ли чёрная фигура атаковать белую
def move_exists(init_x: int, init_y: int, mov_x: int, mov_y: int, figure: bool) -> bool:
    horizontal = horizontal_move(init_y, mov_y)
    vertical = verical_move(init_x, mov_x)
    diagonal = diagonal_move(init_x, init_y, mov_x, mov_y)

    # если белая фигура - ферзь
    if figure:
        if horizontal or vertical or diagonal:
            return True    
    # если белая фигура - ладья
    else:
        if horizontal or vertical:
            return True
    return False
# move_exists

"""
def end_program():
    print("Программа завершиться через 3 секунды")
    sleep(3)
    exit()
"""

def end_program():
    print("\n\t\tПрограмма завершена")
    print("\t-- Нажмите на [Enter] для выхода --")
    input()
    exit()
# end_program

def get_figure_type(console_text: str) -> bool:

    print(console_text, end='')
    figure = input()
    try:
        figure = int(figure)
    except ValueError:
        print("Необходимо ввести число!")
        end_program()
    
    if figure == 1:
        return True
    elif figure == 2:
        return False
    else:
        print("Это число не ожидалось")
        end_program()
# get_figure_type

def get_figure_coordinates(console_text: str) -> list:

    print(console_text)
    print("Положение по x: ", end='')
    x = input()
    print("Положение по y: ", end='')
    y = input()

    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print("Необходимо ввести числа!")
        end_program()

    if (1 <= x <= 8) and (1 <= y <= 8):
        return [x, y]
    else:
        print("\nЧисла должны быть в диапазоне от 1 до 8 включительно!")
        end_program()
# get_figure_coordinates

print("Задание 2")
print("Эта программа проверяет, может ли белая фигура, совершив свой ход, не попасть под удар")
print("Доступные фигуры: ферзь и ладья\n")

white_text = "Выберите, чем будет белая фигура:\n1 - ферзь\n2 - ладья\nВаш ответ: "
black_text = "Выберите, чем будет чёрная фигура:\n1 - ферзь\n2 - ладья\nВаш ответ: "

white_fig_init_pos_text = "Введите координаты изначального положения белой фигуры"
black_fig_pos_text = "Введите координаты положения чёрной фигуры"
white_fig_move_pos_text = "Введите координаты положения белой фигуры после хода"

# получение данных о фигурах от пользователя
white_fig = get_figure_type(white_text)
print('\n')
black_fig = get_figure_type(black_text)
print('\n')

print("Числа должны быть в диапазоне от 1 до 8 включительно")

# изначальное положение белой фигуры
white_init_pos = get_figure_coordinates(white_fig_init_pos_text)
print('\n')
# положение чёрной фигуры
black_pos = get_figure_coordinates(black_fig_pos_text)
print('\n')
# новое положение белой фигуры после хода
white_mov_pos = get_figure_coordinates(white_fig_move_pos_text)

if not move_exists(white_init_pos[0], white_init_pos[1], white_mov_pos[0], white_mov_pos[1], white_fig):
    print("Такой ход белой фигурой невозможен")
    end_program()

if move_exists(black_pos[0], black_pos[1], white_mov_pos[0], white_mov_pos[1], black_fig):
    print('\n\t'+"Белая фигура под ударом")
else:
    print('\n\t'+"Белая фигура в безопасности")

end_program()