import sys


def show_size(x):
    return sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key)
                show_size(value)
        elif not isinstance(x, str):
            for item in x:
                show_size(item)

def calc_size(n):
    calc_s = 0
    
    for i in n:
        show_size(i)
        calc_s += sys.getsizeof(i)
    print(f'Размер переменных: {calc_s}')


# Во втором массиве сохранить индексы четных элементов первого массива.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

#print(array)

result = []
for i in range(len(array)):
    if array[i] % 2 == 0:
        result.append(i)
#print(f'Индексы четных элементов: {result}')

result_new = [i for i in range(len(array)) if array[i] % 2 == 0]
#print(f'Индексы четных элементов: {result_new}')


variables = [array, result, result_new, i]


calc_size(variables)


#Размер переменных: 250      #SIZE = 10
#Размер переменных: 350      #SIZE = 20
#Размер переменных: 1010     #SIZE = 100
#Python 3.7.1 on win32

#Задача с генерируемым массивом и 2мя циклами самая тяжелая.
#Чем больше SIZE тем тяжелее.
