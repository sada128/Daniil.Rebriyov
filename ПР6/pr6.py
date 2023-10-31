#Вариант 7
#Задание 1
from math import prod

a = [1,2,3,4,5,6]

s = sum(a[1::2])

x = prod(a[::2])

print("Произведение:",x)

print ("Сумма : ", s)
#Задание 2
arr = list(int, input('>>').split())
 
# Определяем индексы максимального и минимального элементов массива
max_index, min_index = arr.index(max(arr)), arr.index(min(arr))
 
# Меняем их местами
arr[max_index], arr[min_index] = arr[min_index], arr[max_index]
print(arr)