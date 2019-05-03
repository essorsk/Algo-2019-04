#3.В массиве случайных целых чисел поменять местами
# минимальный и максимальный элементы.

import random

array = [random.randint(0, 100) for _ in range(10)]
print(array)

max_, min_, pos_max, pos_min = 0, 0, 0, 0

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
array[pos_min] = max_
array[pos_max] = min_
print(array)
