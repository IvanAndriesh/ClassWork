from functools import reduce
from operator import mul
import random
#Задание 30
def ee(stolbi, stroki):
    B = []
    plus_spisok = []
    otvet = 0
    for stolb in range(stolbi):
        matrix_numb = []
        for stroka in range(stroki):
            matrix_numb.append(random.randint(-10, 10))
        for i in matrix_numb:
            if i > 0:
                plus_spisok.append(i)
        B.append(matrix_numb)
    for vivod in B:
        print(vivod)
    print("Произведение положительных эллементов равно: ", reduce(mul, plus_spisok))
print(ee(int(input("Введите количество столбцов матрицы: ")),int(input("Введите количество строк матрицы: "))))

#Задание 31
def ee(stolbi, stroki):
    B = []
    Min_zn = 0 
    for stolb in range(stolbi):
        matrix_numb = []
        for stroka in range(stroki):
            matrix_numb.append(random.randint(-10, 10))
        for i in matrix_numb:
            if i < Min_zn:
                Min_zn = i
                index = matrix_numb.index(Min_zn)
        B.append(matrix_numb)
    for vivod in B:
        print(vivod)
    print("Минимальный элемент матрицы:",Min_zn, "Индекс:", index)
print(ee(int(input("Введите количество столбцов матрицы: ")),int(input("Введите количество строк матрицы: "))))

#Задание 32
def ee(stolbi, stroki):
    B = []
    Min_zn = 0
    index_mn = []
    Max_zn = 0
    index_mx = []
    for stolb in range(stolbi):
        matrix_numb = []
        for stroka in range(stroki):
            matrix_numb.append(random.randint(-10, 10))
        B.append(matrix_numb)
    for i in range(stolbi):
        for j in range(stroki):
            if B[i][j] < Min_zn:
                Min_zn = B[i][j]
                index_mn = [i, j]
            if B[i][j] > Max_zn:
                Max_zn = B[i][j]
                index_mx = [i, j]
    print("МАТРИЦА")
    for vivod in B:
        print(vivod)
    print("Минимальный эллемент:", Min_zn, "Индекс", index_mn)
    print("Максимальный эллемент:", Max_zn, "Индекс", index_mx)
    B[index_mn[0]][index_mn[1]], B[index_mx[0]][index_mx[1]] = B[index_mx[0]][index_mx[1]], B[index_mn[0]][index_mn[1]]
    print("МАТРИЦА С ЗАМЕНЕНЫМИ ЭЛЕМЕНТАМИ")
    for vivod in B:
        print(vivod)
    print("Минимальный эллемент:", Min_zn, "Индекс", index_mn)
    print("Максимальный эллемент:", Max_zn, "Индекс", index_mx)

ee(int(input("Введите количество столбцов матрицы: ")), int(input("Введите количество строк матрицы: ")))

#Задание 33
def ee(stolbi, stroki):
    B = []
    for stolb in range(stolbi):
        matrix_numb = []
        for stroka in range(stroki):
            matrix_numb.append(random.randint(-10, 10))
        B.append(matrix_numb)

    for vivod in B:
        print(vivod)

    umno = []
    for i in range(stolbi):
        product = 1
        for j in range(stroki):
            product *= B[j][i]
        umno.append(product)

    print("Одномерный массив из произведений элементов каждого столбца матрицы:", umno)

ee(int(input("Введите количество столбцов матрицы: ")), int(input("Введите количество строк матрицы: ")))

#Задание 34
def ee(stolbi, stroki):
    B = []
    for stolb in range(stolbi):
        matrix_numb = []
        for stroka in range(stroki):
            matrix_numb.append(random.randint(-10, 10))
        B.append(matrix_numb)

    for vivod in B:
        print(vivod)

    otr_el = []
    for i in range(stolbi):
        otr_count = 0
        for j in range(stroki):
            if B[i][j] < 0:
                otr_count += 1
        otr_el.append(otr_count)

    print("Одномерный массив из количеств отрицательных элементов каждой строки матрицы:", otr_el)

ee(int(input("Введите количество строк матрицы: ")), int(input("Введите количество столбцов матрицы: ")))
