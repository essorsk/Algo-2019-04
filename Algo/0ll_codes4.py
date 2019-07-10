# Найти сумму и произведение цифр введённого пользователем трехзначного числа
import sum_memory


num = input('Введите трёхзначное число: ')

# решение через долнительные переменные
num = int(num)
a = num // 100
b = num % 100 // 10
c = num % 10
summ = a + b + c
print(f'Сумма = {summ}')
print(f'Произведение = {a * b * c}')

sum_mem = sum_memory.SumMemory()
sum_mem.extend(num, a, b, c, summ)
sum_mem.print_sum()

# решение через цикл
num = str(num)
summa = 0
mult = 1
for i in num:
    summa += int(i)
    mult *= int(i)
print(f'Сумма = {summa}')
print(f'Произведение = {mult}')

sum_mem = sum_memory.SumMemory()
sum_mem.extend(num, summa, mult, i)
sum_mem.print_sum()



# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
import sys

# вариант 1
num = int(input('Введите целое число: '))
print(sys.getsizeof(num))
even, odd = 0, 0

while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10

print(sys.getsizeof(even))
print(sys.getsizeof(odd))
print(f"четных - {even}, нечетных - {odd}")

# вариант 2
sum_ = 0
num = int(input('Введите целое число: '))
sum_ += sys.getsizeof(num)
even, odd = 0, 0

while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10

sum_ += sys.getsizeof(even)
sum_ += sys.getsizeof(odd)
print(f"четных - {even}, нечетных - {odd}")
print(sum_)


# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

from sum_memory_2 import sum_memory


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

idx_min = 0
idx_max = 0
for i in range(len(array)):
    if array[i] < array[idx_min]:
        idx_min = i
    elif array[i] > array[idx_max]:
        idx_max = i
print(f'Min = {array[idx_min]} в ячейке {idx_min};\n'
      f'Max = {array[idx_max]} в ячейке {idx_max}')

array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
print(array)

print(locals())     # пример того как выглядит "локальный 'словарь'"
print('*' * 50)
print(sum_memory(locals()))


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



# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = int(input('Введите целое число: '))
even, odd = 0, 0
while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10
print(f"четных - {even}, нечетных - {odd}")


variables = [even, odd, num]

calc_size(variables)

import sys
#адрес объекта внутри памяти
a = 42
b = a
#уменьшение объектов
del b
print(id(a))
#счетчик ссылок
print(sys.getrefcount(a))
#Сколько байт хранится в памяти
print(sys.getsizeof(a))

def show_size(x, level=0):
    print('\t' * level, f'type = {type(x)}, size = {sys.getsizeof(x)}, obj = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level+1)
                show_size(value, level+1)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)

num = 4678367672316523
even, odd = 0, 0
while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10
print(f"четных - {even}, нечетных - {odd}")

show_size(num)

show_size(odd)
show_size(even)

import sys
import ctypes
import struct

a = 42
#show id
print(id(a))
#show size
print(sys.getsizeof(a))
#show object directly from OS in string by id & size
print(ctypes.string_at(id(a), sys.getsizeof(a)))

#
#print(struct.unpack('LLLLLLl',ctypes.string_at(id(a), sys.getsizeof(a)))) 


# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# (в рамках первых трех уроков)

import sys


class SumMemory:

    def __init__(self):
        """
        _sum_memory - общее количество занятой памяти
        _types - словарь вида {'type': [count, size]}
        """
        self._sum_memory = 0
        self._types = {}

    def extend(self, *args):
        for obj in args:
            self._add(obj)

    def _add(self, obj):
        spam = sys.getsizeof(obj)
        eggs = str(type(obj))
        self._sum_memory += spam
        if eggs in self._types:
            self._types[eggs][0] += 1
            self._types[eggs][1] += spam
        else:
            self._types[eggs] = [1] * 2
            self._types[eggs][1] = spam

        if hasattr(obj, '__iter__'):
            if hasattr(obj, 'items'):
                for key, value in obj.items():
                    self._add(key)
                    self._add(value)
            elif not isinstance(obj, str):
                for item in obj:
                    self._add(item)

    def print_sum(self):
        print(f'Переменные заняли в сумме {self._sum_memory} байт')
        for key, value in self._types.items():
            print(f'Объекты класса {key} в количестве {value[0]} заняли {value[1]} байт')


# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# (в рамках первых трех уроков)

import sys


def sum_memory(objects):
    sum_mem = 0
    unique_id = set()
    for key, value in objects.items():
        if key.startswith('__'):
            # убираем "магию"
            continue
        elif hasattr(value, '__call__'):
            # убираем функции
            continue
        elif hasattr(value, '__loader__'):
            # убираем модули
            continue
        elif id(value) in unique_id:
            # убираем объекты (переменные), которые уже попали в сумму
            continue
        else:
            """
            Тут должен быть крутой цикл из прошлого примера
            """
            unique_id.add(id(value))
            sum_mem += sys.getsizeof(value)
            print(f'переменная {key} класса {type(value)} хранит {value} '
                  f'и занимает {sys.getsizeof(value)} байт')

    return sum_mem

allocated = 0

for new_size in range(1000):
    if allocated < new_size:
        new_allocated = (new_size >> 3) + (3 if new_size < 9 else 6)
        allocated = new_size + new_allocated
    print(f'size - {new_size} \tallocated - {allocated}')


import sys
from collections import deque

a = 5
b = a
c = a
del b
print(id(a))
print(sys.getrefcount(a))
print(sys.getsizeof(a))


def show_size(x, level=0):
    print('\t' * level, f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)


d = [i for i in range(10)]
show_size(d)

e = 'Привет мир!'
show_size(e)

f = tuple(d)
show_size(f)

g = deque(d)
show_size(g)

h = set(d)
show_size(h)

m = {str(i): i for i in range(10)}
show_size(m)

import sys
import ctypes
import struct

a = 'Hello world!'
b = a
c = a
print(id(a))
print(sys.getsizeof(a))
print(ctypes.string_at(id(a), sys.getsizeof(a)))
print(struct.unpack('LLLLLLLLLLli' + 'c' * 13, ctypes.string_at(id(a), sys.getsizeof(a))))
print(id(int))
print(id(object))
print(id(str))

lst = [0, 1, 2, 3]
# range(40000) == range(4)






