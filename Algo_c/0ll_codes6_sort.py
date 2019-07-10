
# Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Вывести на экран исходный и отсортированный массивы.

import random


def bubble_sort(array, reverse=False):
    #Если реверс тру, то 1, если ложь, то -1
    sign = int(reverse) * 2 - 1
    n = 1

    while n < len(array):
        is_sorted = True
        for i in range(len(array) - n):
            if array[i] * sign < array[i + 1] * sign:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False

        if is_sorted:
            break

        n += 1
        print(array)


SIZE = 10
LIMIT = 100
data = [random.randrange(-LIMIT, LIMIT) for _ in range(SIZE)]
print(data)
bubble_sort(data, reverse=True)
print(data)


# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random, math


def merge_sort(array):

    if len(array) <= 1:
        return array

    # необязательное дополненение
    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array

    left = merge_sort(array[:len(array) // 2])
    right = merge_sort(array[len(array) // 2:])
    i, j = 0, 0
    #На этом этапе возвращаются 2 маленьких гарантированно отсортированных кусочка массива

    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            array[i + j] = left[i]
            i += 1
        else:
            array[i + j] = right[j]
            j += 1

    while len(left) > i:
        array[i + j] = left[i]
        i += 1
    while len(right) > j:
        array[i + j] = right[j]
        j += 1

    return array


SIZE = 10
LIMIT = 50
data = [random.uniform(0, LIMIT) for _ in range(SIZE)]
# data = [round(random.uniform(0, LIMIT), 2) for _ in range(SIZE)]    # round для простоты визуальной проверки
print(data)
merge_sort(data)
print(data)
# print(math.floor(49.9999))

# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше ее.

import random


# вариант 1
def median_square(array):
    for i in range(len(array)):
        smaller = equal = bigger = 0
        for j in range(len(array)):
            if array[i] < array[j]:
                smaller += 1
            elif array[i] > array[j]:
                bigger += 1
            else:
                equal += 1
        equal -= 1

        if smaller == bigger or smaller == equal + bigger or smaller + equal == bigger:
            return array[i]


# вариант 2
def partition(array, pivot):
    smaller = []
    equally = []
    bigger = []
    for item in array:
        if item < pivot:
            smaller.append(item)
        elif item > pivot:
            bigger.append(item)
        else:
            equally.append(item)
    return smaller, equally, bigger


def top_key(array, key):
    pivot = array[random.randrange(len(array))]
    left, middle, right = partition(array, pivot)

    if len(left) == key:
        return left
    if len(left) < key <= len(left) + len(middle):
        return middle
    if len(left) > key:
        return top_key(left, key)
    return top_key(right, key - len(left) - len(middle))


def median(array):
    result_list = top_key(array, len(array) // 2 + 1)
    return max(result_list)


SIZE = 4
LIMIT = 100
data = [random.randrange(0, LIMIT) for _ in range(2 * SIZE + 1)]
print(data)
print(f'mediana_square = {median_square(data)}')
print(data)
print(f'mediana = {median(data)}')
print(data)
print(sorted(data))


# вариант 3
import statistics

print('*' * 50)
print(data)
print(f'mediana = {statistics.median(data)}')
print(sorted(data))

import random

SIZE = 10
array = [i for i in range(SIZE)]
print(array)
random.shuffle(array)
print(array)

# size = 2*m+1


array = [0, 5, 8, 6, 4, 7, 3, 1, 9, 2]

n = 1

while n < len(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    n += 1
    print(array)

print(array)


def selection_sort(array):
    for i in range(len(array)):
        idx_min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j

            array[idx_min], array[i] = array[i], array[idx_min]


array_ddd = [0, 5, 8, 6, 4, 7, 3, 1, 9, 2]
selection_sort(array_ddd)
print(array_ddd)

def insertion_sort(array):
    for i in range(1, len(array)):
        spam = array[i]
        j = i
        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -= 1

        array[j] = spam
        print(array)


array_ddd = [0, 5, 8, 6, 4, 7, 3, 1, 9, 2]
insertion_sort(array_ddd)
print(array_ddd)


import random


def quick_sort(array, fst, lst):
    if fst >= lst:
        return

    pivot = array[random.randint(fst, lst)]
    i, j = fst, lst

    while i <= j:
        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    print(array)
    quick_sort(array, fst, j)
    quick_sort(array, i, lst)


array_ddd = [0, 5, 8, 6, 4, 7, 3, 1, 9, 2]
quick_sort(array_ddd, 0, len(array_ddd) - 1)
print(array_ddd)

import random

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = random.choice(array)
    small = []
    medium = []
    large = []

    for item in array:
        if item < pivot:
            small.append(item)
        elif item == pivot:
            medium.append(item)
        elif item > pivot:
            large.append(item)

    print(small, medium, large)
    return quick_sort(small) + medium + quick_sort(large)


array_ddd = [0, 5, 8, 6, 4, 7, 3, 1, 9, 2]
new_array = quick_sort(array_ddd)
print(array_ddd)
print(new_array)

def shell_sort(array):
    assert len(array) < 4000, "Массив слишком большой"

    def new_icrement(array):
        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750] #основано на стат
        while len(array) <= inc[-1]:  #последний элемент
            inc.pop()  #убираем слишком большие шаги
        while len(inc) > 0:
            yield inc.pop()  #возвращаем последний элемент и запоминает позицию

    for increment in new_icrement(array):
        for i in range(increment, len(array)):
            for j in range(i, increment - 1, -increment):
                if array[j - increment] <= array[j]:
                    break
                array[j], array[j - increment] = array[j - increment], array[j]
        print(array)


array_ddd = [0, 5, 8, 6, 4, 7, 3, 1, 9, 2]
shell_sort(array_ddd)
print(array_ddd)

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'name={self.name}; age={self.age}'


p1 = Person('Pete', 33)
p2 = Person('Vasya', 35)
p3 = Person('Jonh', 25)
p4 = Person('Mary', 34)
people = [p1, p2, p3, p4]

print(people)


def by_name(person):
    return person.name


a = sorted(people, key=by_name)
print(a)

#Сахар
from operator import attrgetter

b = sorted(people, key=attrgetter('age'))
print(b)






