# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.

import random
n = int(input("Введите количество элементов массива: "))
x = int(input("Введите произвольное число: "))
array = [random.randint(x-10, x+10) for i in range(n)]
print(array)


min_set = set()
min = abs(x-array[0])
elem = array[0]
for i in range(n):
    if abs(x-array[i]) < min and array[i]!=x:
        min = abs(x-array[i])
        elem = array[i]
min_set.add(elem)
for i in range(n):
    if abs(x-array[i]) == min and array[i]!=x:
        min = abs(x-array[i])
        elem = array[i]
        min_set.add(elem)

print(f"Ближайшие к числу {x} числа из заданного массива {min_set}.")
