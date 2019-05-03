#6.	В одномерном массиве найти сумму элементов,
#находящихся между минимальным и максимальным элементами.
#Сами минимальный и максимальный элементы в сумму не включать.

import random

array = [random.randint(0, 100) for _ in range(10)]
print(array)

max_, min_, pos_max, pos_min, sum_ = 0, 0, 0, 0, 0

if array[0] < array[1]:
    min_ = array[0]
    max_ = array[1]
    pos_min = 0
    pos_max = 1
else:
    min_ = array[1]
    max_ = array[0]
    pos_min = 1
    pos_max = 0

for i in range(2, len(array)):
    if array[i] < min_:
        min_ = array[i]
        pos_min = i
    elif array[i] > max_:
        max_ = array[i]
        pos_max = i

if (pos_max - pos_min) > 1:
    for i in range ((pos_min +1), pos_max):
        sum_ += array[i]
elif (pos_min - pos_max) > 1:
    for i in range ((pos_max +1), pos_min):
        sum_ += array[i]
else:
    print('Минимальный и максимальный элемент массива расположены рядом.')
       
print(f' Сумма элементов между максимальным {max_} и минимальным {min_} элементами: {sum_}')
