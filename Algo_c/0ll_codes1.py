# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа должна не завершаться, а запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа сообщает ему об ошибке и снова запрашивает знак операции.
# Также пользователю нужно сообщать о невозможности деления на ноль, если он ввел 0 в качестве делителя.


while True:
    sign = input("Знак (+,-,*,/,0): ")
    if sign == '0':
        break
    # if sign == '+' or sign == '-' or sign == '*' or sign == '/':
    if sign in {'+', '-', '*', '/'}:  # так нельзя было делать в ДЗ
        x = float(input("x = "))
        y = float(input("y = "))
        if sign == '+':
            print(f'{x + y:.2f}')
        elif sign == '-':
            print(f'{x - y:.2f}')
        elif sign == '*':
            print(f'{x * y:.2f}')
        elif sign == '/':
            if y != 0:
                print(f'{x / y:.2f}')
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")


# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# вариант 1
num = int(input('Введите целое число: '))
even, odd = 0, 0
while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10
print(f"четных - {even}, нечетных - {odd}")


# вариант 2, который не надо было сдавать!!!
num = input('Введите целое число: ')
even = odd = 0
for i in num:
    if i in {'0', '2', '4', '6', '8'}:
        even += 1
    else:
        odd += 1
print(f"четных - {even}, нечетных - {odd}")

# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

# вариант 1
num = int(input('Введите целое число: '))
result = 0
while num > 0:
    result = result * 10 + num % 10
    num = num // 10
print(result)

# вариант 2, это не для ДЗ
num = input('Введите целое число: ')
result = ''
for i in num:
    result = i + result
print(result)

# вариант 3, и это не для ДЗ
num = input('Введите целое число: ')
result = num[::-1]
print(result)

# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125, ...
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Сколько элементов сложить: '))
item = 1
sum_ = 0
for _ in range(n):
    sum_ += item
    item /= -2      # item *= -0.5
print(sum_)

# вариант с геометрической прогрессией
summa_2 = 1 * (1 - (-0.5) ** n) / (1 - (-0.5))
print(summa_2)

# рассказать про плохие имена переменных
b = sum([2, 4, 6])


# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
START = 32
STOP = 127

for i in range(START, STOP + 1):
    print(f'\t{i}-{chr(i)}', end='')
    if i % 10 == 1:
        print()

# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

import random

num = random.randint(0, 100)
print("Отгадайте число от 0 до 100 за 10 попыток")
for i in range(1, 11):
    answer = int(input(f'Попытка {i}: '))
    if num < answer:
        print('Число меньше')
    elif num > answer:
        print('Число больше')
    else:
        print(f'Вы угадали с {i}-й попытки')
        break
else:
    print(f'Поражение. Было загадано {num}')


# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.


def sum_natural(n):
    assert n < 999, 'Слишком большое число'
    if n == 1:
        return n
    sum_n = n + sum_natural(n - 1)
    return sum_n


n = int(input('Введите любое натуральное число: '))

left = sum_natural(n)
right = n * (n + 1) // 2

print(left)
print(right)
print(left == right)

# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

num = int(input("Введите количество чисел: "))
digit = int(input("Какую цифру подсчитать: "))
count = 0
for i in range(1, num + 1):
    ans = int(input(f'Введите число {i}: '))
    while ans > 0:
        if ans % 10 == digit:
            count += 1
        ans //= 10

print(f'Было введено {count} цифр {digit}')

# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


def sum_digits(number):
    if number < 10:
        return number
    return number % 10 + sum_digits(number // 10)


num = int(input('Введите натуральное число. Ноль - выйти   '))
max_sum = 0
max_num = 0
while num != 0:
    spam_num = num
    spam_sum = sum_digits(num)
    if spam_sum > max_sum:
        max_sum = spam_sum
        max_num = spam_num
    num = int(input('Введите натуральное число. Ноль - выйти   '))
print(f'Число {max_num} имеет максимальную сумму цифр: {max_sum}')



# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

START_NUM = 2
END_NUM = 99
START_DIV = 2
END_DIV = 9
# вариант 1
for i in range(START_DIV, END_DIV + 1):
    frequency = 0
    for j in range(START_NUM, END_NUM + 1):
        if j % i == 0:
            frequency += 1
    print(f'Числу {i} кратно {frequency} чисел')

# вариант 2
print('вариант 2')
frequency = [0] * (END_DIV - START_DIV + 1)  # [0] * 8
for i in range(START_NUM, END_NUM + 1):
    for j in range(START_DIV, END_DIV + 1):
        if i % j == 0:
            frequency[j - START_DIV] += 1

for i, item in enumerate(frequency, start=START_DIV):
    print(f'Числу {i} кратно {item} чисел')


# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 0, 3, 4, 5 (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# array = [random.randint(MIN_ITEM, MAX_ITEM)] * SIZE
#  показать всем, что так не работает!!!
print(array)

result = []
for i in range(len(array)):
    if array[i] % 2 == 0:
        result.append(i)
print(f'Индексы четных элементов: {result}')

result_new = [i for i in range(len(array)) if array[i] % 2 == 0]
print(f'Индексы четных элементов: {result_new}')



# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

N = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(N)]
print(array)

# 1 вариант
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

print('=' * 20)

# 2 вариант как пример асимптотической сложности
# O(n) против O(n) * (1 + 1 + 0.5 + 0.5)
min_num = min(array)
max_num = max(array)
idx_min = array.index(min_num)
idx_max = array.index(max_num)
print(f'Min = {array[idx_min]} в ячейке {idx_min};\n'
      f'Max = {array[idx_max]} в ячейке {idx_max}')
array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
print(array)


# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 0
array = [random.randint(MIN_ITEM, SIZE // 1.5) for _ in range(SIZE)]
print(array)

# вариант 1
num = array[0]
frequency = 1
for i in range(len(array)):
    spam = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            spam += 1
    if spam > frequency:
        frequency = spam
        num = array[i]

if frequency > 1:
    print(f'Число {num} встречется {frequency} раз(а)')
else:
    print('Все элементы уникальны')

# ваниант 2
counter = {}
frequency = 1
num = None
for item in array:
    if item in counter:
        counter[item] += 1
    else:
        counter[item] = 1
    if counter[item] > frequency:
        frequency = counter[item]
        num = item

if num is not None:
    print(f'Число {num} встречется {frequency} раз(а)')
else:
    print('Все элементы уникальны')

# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

SIZE = 10
MIN_ITEM = -800
MAX_ITEM = -750
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# вариант 1
i = 0
index = -1
while i < len(array):   # или for i in range(len(array)):
    if array[i] < 0 and index == -1:
        index = i
    elif 0 > array[i] > array[index]:
        index = i
    i += 1

if index != -1:
    print(f'Максимальное отрицательное число {array[index]} '
          f'находится в ячейке {index}')

# вариант 2
num = float('-inf')
for i, item in enumerate(array):
    if 0 > item > num:
        num = item
        index = i

if num != float('-inf'):
    print(f'Максимальное отрицательное число {num} '
          f'находится в ячейке {index}')

# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

idx_min = 0
idx_max = 0
for i in range(1, len(array)):
    if array[i] < array[idx_min]:
        idx_min = i
    elif array[i] > array[idx_max]:
        idx_max = i

if idx_min > idx_max:
    idx_min, idx_max = idx_max, idx_min

print(f'Левая граница: {array[idx_min]}\n'
      f'Правая граница: {array[idx_max]}')

summ = 0
for i in range(idx_min + 1, idx_max):
    summ += array[i]
print(f'Сумма = {summ}')


# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# вариант 1
min_first, min_second = (0, 1) if array[0] > array[1] else (1, 0)
# if array[0] > array[1]:
#     min_first = 0
#     min_second = 1
# else:
#     min_first = 1
#     min_second = 0

for i in range(2, len(array)):
    if array[i] < array[min_first]:
        spam = min_first
        min_first = i
        if array[spam] < array[min_second]:
            min_second = spam

    elif array[i] < array[min_second]:
        min_second = i

print(f'Число {array[min_first]} в ячейке {min_first}')
print(f'Число {array[min_second]} в ячейке {min_second}')

# вариант 2 только число, позиция и сохранность данных не важны
min_1 = min(array)
array.remove(min_1)
min_2 = min(array)
print(min_1, min_2)



# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и
# записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу.

N = 5
M = 4
matrix = []
for i in range(N):
    row = []
    summ = 0

    for j in range(M - 1):
        num = int(input(f'{i}-я строка, {j}-й элемент : '))
        summ += num
        row.append(num)

    row.append(summ)
    matrix.append(row)

for line in matrix:
    print(line)

# O(N*M)
# O(N*N) = O(N**2)

# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE = 3
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)] for _ in range(SIZE)]

for line in matrix:
    print(*line, sep='\t')


max_ = None

for j in range(len(matrix[0])):
    min_ = matrix[0][j]

    for i in range(len(matrix)):
        if matrix[i][j] < min_:
            min_ = matrix[i][j]

    if max_ is None or max_ < min_:
        max_ = min_

print(f'Max in min = {max_}')


# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random
import cProfile


def max_below_zero(size):
    # SIZE = 10
    array = [random.randint(size * -10, size * 10) for _ in range(size)]
    # print(array)

    i = 0
    index = -1

    while i < size:
        if array[i] < 0 and index == -1:
            index = i
        elif 0 > array[i] > array[index]:
            index = i

        i += 1

    # print(f'Число {array[index]} на позиции {index}')
    return f'Число {array[index]} на позиции {index}'


# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random
import cProfile


def max_below_zero(array):
    # SIZE = 10
    # print(array)

    i = 0
    index = -1

    while i < size:
        if array[i] < 0 and index == -1:
            index = i
        elif 0 > array[i] > array[index]:
            index = i

        i += 1

    # print(f'Число {array[index]} на позиции {index}')
    return f'Число {array[index]} на позиции {index}'


size = 1000
array = [random.randint(size * -10, size * 10) for _ in range(size)]



# Sieve Eratosfen
import cProfile
import math


# pi_f = x / math.log(x)


def prime(num):
    assert num <= 5761455, 'Слишком большой аргумент'
    # if num > 5761455:
    #     raise Exception('Слишком большой аргумент')
    pi_func = {4: 10,
               25: 10 ** 2,
               168: 10 ** 3,
               1229: 10 ** 4,
               9592: 10 ** 5,
               78498: 10 ** 6,
               664579: 10 ** 7,
               5761455: 10 ** 8,
               }
    for key in pi_func.keys():
        if num <= key:
            size = pi_func[key]
            break

    array = [i for i in range(size)]

    array[1] = 0
    for i in range(2, size):
        if array[i] != 0:
            # j = i + i
            j = i ** 2
            while j < size:
                array[j] = 0
                j += i

    res = [i for i in array if i != 0]
    return res[num - 1]


def test_prime(func):
    real_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                  103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                  211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                  331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                  449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
                  587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                  709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
                  853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
                  991, 997, 1009, 1013]

    for i, item in enumerate(real_prime, start=1):
        assert func(i) == item, f'Test {i} fail\t func({i}) = {func(i)}'
        print(f'Test {i} OK')


# test_prime(prime)
print(prime(10))
# cProfile.run('prime(10)')


# Cool Sieve
import cProfile
import math
import timeit


def prime(num):
    MULTIPLIER = 1.5
    size = int(num * math.log(num) * MULTIPLIER) if num > 3 else 6

    array = [True for _ in range(size)]
    array[:2] = [False, False]
    count = 0

    for i in range(2, size):
        if array[i]:

            count += 1
            if count == num:
                return i

            for j in range(i ** 2, size, i):
                array[j] = False


def test_prime(func):
    real_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                  103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                  211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                  331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                  449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
                  587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                  709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
                  853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
                  991, 997, 1009, 1013]

    for i, item in enumerate(real_prime, start=1):
        assert func(i) == item, f'Test {i} fail\t func({i}) = {func(i)}'
        print(f'Test {i} OK')


test_prime(prime)
print(timeit.timeit('prime(10000000)', globals=globals(), number=1))  # Ответ: 179424673 Время: 59.5142517372963
# cProfile.run('prime(10)')



# Prime numbers without sieve Eratosfen
import cProfile


def prime(num):
    count = 1
    current_prime = 2

    while count < num:
        current_prime += 1
        # for i in range(2, current_prime):
        for i in range(2, int(current_prime ** 0.5) + 1):
            if current_prime % i == 0:
                break
        else:
            count += 1

    return current_prime


def test_prime(func):
    real_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                  103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                  211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                  331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                  449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
                  587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                  709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
                  853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
                  991, 997, 1009, 1013]

    for i, item in enumerate(real_prime, start=1):
        assert func(i) == item, f'Test {i} fail\t func({i}) = {func(i)}'
        print(f'Test {i} OK')


test_prime(prime)
print(prime(1))
# cProfile.run('prime(10)')       # 0


























