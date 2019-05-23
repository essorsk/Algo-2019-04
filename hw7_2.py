#2 Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
#заданный случайными числами на промежутке [0; 50).
#Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10
array = [random.randint(0, 49) for _ in range(SIZE)]
print(array)


#merge sort with recursia in 2 functions


#main function
def mergesort(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    left = mergesort(arr[:middle])
    right = mergesort(arr[middle:])
    return merge(left, right)
           

#support function
def merge(left, right):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

print(mergesort(array))
