# Лабораторная работа №13
# Вариант 6
# Гаврилов Павел ФМ-11-25

import random as rnd    # для randint и seed
import time             # для time() как сид для рандома но не судьба, пока

import os

DIR_PATH = "lab13-files"

def rand_matrix(
        row:        int = 6,
        colomn:     int = 6,
        seed:       int = 0,
        min_value:  int = -10,
        max_value:  int = 10
        ) -> list:
# begin 
    rnd.seed(seed)
    read_mtx = []
    for i in range(row):
        read_mtx += [[rnd.randint(min_value, max_value) for _ in range(colomn)]]
    return read_mtx
# !rand_matrix(int, int, int, int, int) -> list

def mtx_to_str(input: list) -> str:
    read_mtx = ''
    for i in range(len(input)):
        for j in range(len(input[i])):
            read_mtx += str(input[i][j]) + ' '
        read_mtx += '\n'
    return read_mtx
# !mtx_to_str(list) -> str

def list_to_str(input: list) -> str:
    read_list = ''
    for i in input:
        read_list += str(i) + ' '
    return read_list + '\n'
# !list_to_str(list) -> str

# seed = int(time.time() * 1000) % 100000
seed = 0
lst = rand_matrix(seed=seed)         # генерация случайной матрицы

# Все файлы будут храниться в директории 'lab 13 files'
# Это проверка на наличие данной директории
# Если её нет, то она будет создана
if not os.path.exists(DIR_PATH):    # Если нет директории
    os.mkdir(DIR_PATH)              # Создать директорию

# writting the matrix to file
fout = open(DIR_PATH + "\\" + "matrix.txt", "w")
fout.write(mtx_to_str(lst))
fout.close()
print(mtx_to_str(lst))
del lst # Удаление ссылок на этот список

# reading matrix from file
read_mtx = []

fin = open(DIR_PATH + "\\" + "matrix.txt", "r")
lines = fin.readlines()
res = []
mult = 1
for line in lines:
    tmp = []
    for elem in line.split():
        elem = int(elem)
        tmp += [elem]
        if elem < 0:
            res += [elem]
            mult *= elem
    read_mtx += [tmp]

str_to_write = list_to_str(res) + str(mult)
fres = open(DIR_PATH + "\\" + "results.txt", "w")
fres.write(str_to_write)
fres.close()