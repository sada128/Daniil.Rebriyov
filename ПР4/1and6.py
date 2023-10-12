#Задание 1
A = int(input())
B = int(input())

for i in range(A, B+1):
    print(i)
#Задание 6
res = 1
n = int(input())
for i in range(1, n + 1):
    res *= i
print("Факториал равен", res)
