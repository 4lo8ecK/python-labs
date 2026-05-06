# Лабораторная работа №1
# Вариант 6
# Гаврилов Павел ФМ-11-25
# Код к каждому заданию как для отдельной программы

import math

# задание 1
x = float(input())
y = float(input())
result = math.cos(2 * y) + 3.6 * math.exp(x)

print(result)

# задание 2

i = float(input())
y = float(input())

result = (0.81 * math.cos(i))/(math.log(y) + (2 * (i ** 3)))

print(result)


# задание 3

m = float(input())
x = 1.1

y = math.sin(m + (math.tan(x) ** 3)) ** 2
a = math.sqrt(abs(x))
b = x ** 4 + m ** 2

print(y)
print(a)
print(b)


# задание 4

x = 2.444
y = 0.869
z = -0.166

a = ((x ** (y + 1)) + (math.exp(y - 1))) / (1 + x * abs(y - math.tan(z)))
b = 1 + (abs(y - x) ** 2) + ((abs(y-x) ** 2) / 2) + ((abs(y - x) ** 3) / 3)

print(a)
print(b)
