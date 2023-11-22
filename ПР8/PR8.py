#Вариант 1
#Задание 1 Вычислить сумму и число положительных элементов матрицы A[N, N],
#находящихся над главной диагональю.
import random


pol = 0
s = 0
N = int(input('Ввод: '))
for i in range(N):
    for j in range(i+1, N):
        a_ij = random.randrange(10)
        if a_ij <= 0:
           continue
        if a_ij > 0:
            pol += 1
            s += a_ij

print('Сумма:', s)
print('Число:', pol)

#Задание 2 
#Дана матрица B[N, М]. Найти в каждой строке матрицы
#максимальный и минимальный элементы и поменять их с первым и
#последним элементами строки соответственно.
import random

Y = int(input())
U = int(input())
I = [[random.randrange(10) for i in range(U)] for j in range(Y)] 
for i, row in enumerate(I):
    max = min = 0
    for j, elem in enumerate(row):
        if elem > row[max]:
            max = j
        if elem < row[min]:
            min = j

    row[max], row[0] = row[0], row[max]
   
    row[min], row[-1] = row[-1], row[min]
print(I)