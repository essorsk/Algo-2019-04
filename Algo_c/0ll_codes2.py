# * для перебора элементов в списке
lst = [1, 2, 4]
print(*lst)
# the same, long type:
for i in lst:
    print(i, end=' ')

# цикл вместо дублирования строчек кода
from collections import namedtuple

all_comp = []
Comp = namedtuple('Comp', 'name, p1, p2, p3, p4, total')
num = int(input('num ='))
for i in range (num):
    name = input('name = ')
    spam = []
    for j in range(1, 5):
        spam.append(int(input(f'p{j} = ')))
    all_comp.append(Comp(name, *spam, sum(spam)))

print(all_comp)    


#как ведут себя массивы  разном добавлении
a = [1, 2, 3]
b = a
a = a + [4, 5]
print(a, b, sep='\n')

# += синтаксический сахар для appened
c = [1, 2, 3]
d = c
c += [4, 5]
print(c, d, sep = '\n')

f =[1, 2, 3]
g = f
f.extend([6, 7])
print(f, g, sep = '\n')


# неправильная доска. Так получается изменяемый объект
row = ['_'] * 3
board = [row] * 3
print(board)
board[0][0] = 'x'
print(board)


#Правильная доска. Внутри циклом задаем неизменяемый объект

brd = [['_'] * 3 for _ in range(3)]
print(brd)
brd[0][0] = 'x'
print(brd)

# set изменяемый объекt, frozen set неизменяемый.
#key in dictionary неизменяемый
set_x = {1, 2, 3}
dict_x = {frozenset(set_x): 'hello'}
print(dict_x)

#во 2 случае получился список

tuple_x = ('one', 'two')
for item in tuple_x:
    print(item)

tuple_y = ('one')
for item in tuple_y:
    print(item)


#Алгоритм двоичного поиска
import random

array = [random.randint(0, 100) for _ in range(10)]
#print(array)
# Двоичный поиск возможен только на отсортированном массиве
array.sort()
print(array)

find = int(input('Какое число найти: '))

pos = len(array) // 2
left = 0
right = len(array) - 1

#пока можно рвать книгу
while array[pos] != find and left <= right:
    if find > array[pos]:
        left = pos + 1
    elif find < array[pos]:
        right = pos - 1
    pos = (left + right) // 2

print('Элемент отсутствует' if left > right else f'Позиция элемента: {pos}')


#Алгоритм вставки числа в массив в определенную позицию
import random

array = [random.randint(0, 100) for _ in range(10)]
print(array)

num = int(input('Какое число вставить: '))
pos = int(input('В какую позицию вставить: '))

# Алгоритм из коробки
#array.insert(pos, num)
#print(array)

#Разбор коробки:
array.append(None)
i = len(array) - 1
while i > pos:
    array[i], array[i - 1] = array[i - 1], array[i]
    i -= 1

array[pos] = num
print(array)
#Поиск индекса элемента в массиве.
print(array.index(num))

#Хитрый инсерт. Это создание нового массива. Т.е. + потратили память.

array_new = array[:pos] + [num] + array[pos:]
print(array_new)


#Matrix (list in list)
import random
matrix = [[random.randint(1, 100) for _ in range(5)] for _ in range (3)]
#print(matrix) #print in line

#Classic print:
for line in matrix:
    print(line)

sum_column = [0] * len(matrix[0])
#print(sum_column)

for line in matrix:
    sum_line = 0
    for i, item in enumerate(line):
        sum_line += item
        sum_column[i] += item
        print(f'{item:>5}', end='')   #сдвиг и печать промежуточных
    print(f'    |  {sum_line}')

for item in sum_column:
    print(f'{item:>5}', end='')
        

import time
import timeit

#bad example
start = time.time()
a = [i for i in range(10000)]
delta = time.time() - start
print(delta)

#with timeit = more everage time

print(timeit.timeit('a = [i for i in range(10000)]', number=100))


#with some code strings & globals

x = 10
res = """
b = []
for i in range(1000):
    b.append(i)
"""

print(timeit.timeit(res, number=100, globals=globals()))


import cProfile

def get_sum(array):
    sum_ = 0
    for item in array:
        sum_ += item
    return sum_


def get_len(array):
    return len(array)

def main():
    lst = [i for i in range(10000)]
    len_ = get_len(lst)
    sum_ = get_sum(lst)


cProfile.run('main()')
    
import cProfile
import functools

#Fibonacci sum (n-2) & (n-1)

#Function to test the code
def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

# k3" "task3.fib(5)"
# 100 loops, best of 5: 5.75 usec per loop


#Recursia + cash by @functools.lru_cache()

@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
    
#Test function fib
#test_fib(fib)

print(fib(15))


import cProfile

#Fibonacci sum (n-2) & (n-1)

#Function to test the code
def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


#Recursia+ memory

def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]
        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]

    return _fib_dict(n)
    

cProfile.run('fib_dict(200)')
#test_fib(fib_dict)


import cProfile

#Fibonacci sum (n-2) & (n-1)

#Function to test the code
def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


#Recursia+ cycle

def fib_loop(n):
    if n < 2:
        return n
    first = 0
    second = 1
    for i in range(2, n + 1):
        first, second = second, first + second
    return second 

cProfile.run('fib_loop(100)')
#test_fib(fib_loop)


### Couple of function, united in 1
import cProfile


def get_len(array):
    return len(array)


def get_sum(array):
    sum_ = 0
    for item in array:
        sum_ += item
    return sum_


def main():
    lst = [i for i in range(1000000)]
    len_ = get_len(lst)
    sum_ = get_sum(lst)


cProfile.run('main()')

#Расчетные объемы резерва памяти

allocated = 0

for new_size in range(1000):
    if allocated < new_size:
        new_allocated = (new_size >> 3) + (3 if new_size < 9 else 6)
        allocated = new_size + new_allocated
    print(f'size  = {new_size} \tallocated - {allocated}')















