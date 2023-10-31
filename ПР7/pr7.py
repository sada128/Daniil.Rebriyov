#Вариант 1
#Задание 1
def area(figure, data):
    if figure == 'круг':
        print(data[0])
        res = 3.14*(data[0]**2)
    if figure == 'квадрат':
        a,b = data
        res = a*b
    if figure == 'треугольник':
        res = (a*b)/2
    return ' Площадь {} = {}'.format(figure, res)
    
figure = input('фигура >>>  ')
data = [ float(i) for i in input('данные через пробел >>> ').split()]
print(area(figure, data))
#Задание 2
from functools import reduce  # Функция для свёрки последовательности
from operator import mul  # Функция, перемножающая 2 числа
 
spisok = [16, 15, 9, 14, 13]  # Исходный список
 
result = reduce(mul, spisok)
#                    /\ Список для свёртки
#               /\ Используем умножение
#        /\ Сворачиваем контейнер
print("произведение: ", result)
 
result2 = sum(spisok) / len(spisok)
print("ср. арифметическое: ", result2)