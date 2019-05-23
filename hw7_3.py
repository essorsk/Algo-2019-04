#3 Массив размером 2m + 1, где m — натуральное число,
#заполнен случайным образом. Найдите в массиве медиану.
#Медианой называется элемент ряда, делящий его на две равные части: в одной
#находятся элементы, которые не меньше медианы, в другой — не больше медианы.
#Примечание: задачу можно решить без сортировки исходного массива.
#Но если это слишком сложно, используйте метод сортировки,
#который не рассматривался на уроках (сортировка слиянием также недопустима).

import random
import numpy as np
import copy

m = int(input('Input integer massive size: '))
array = [random.randint(0, 50) for _ in range(2 * m + 1)]
print(array)


#Numpy solution for check
print(f'Numpy median is: {np.median(np.array(array))}')

#For Switzerland Bank

def medi(array):
    arr = copy.deepcopy(array)

    for i in range(m):
        min_e, max_e = (0, 1) if arr[0] < arr[1] else (1, 0)
        for j in range(2, len(arr)):
            if arr[j] < arr[min_e]:
                min_e = j
            elif arr[j] > arr[max_e]:
                    max_e = j
        arr.remove(arr[min_e])
        if min_e < max_e:
            arr.remove(arr[max_e - 1])
        else: arr.remove(arr[max_e])
    print(f'Calculated median is: {arr[0]}')
        
medi(array)
