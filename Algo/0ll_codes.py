# Найти сумму и произведение цифр введённого пользователем трехзначного числа

num = input('Введите трёхзначное число: ')

# решение через долнительные переменные
num = int(num)
a = num // 100
b = num % 100 // 10
c = num % 10
summa = a + b + c
# mult = a * b * c
print(f'Сумма = {summa}')
print(f'Произведение = {a * b * c}')

# решение через цикл
num = str(num)
summa = 0
mult = 1
for i in num:
    summa += int(i)
    mult *= int(i)
print(f'Сумма = {summa}')
print(f'Произведение = {mult}')


# Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат

a = 5
print(f'{a} = {bin(a)}')
b = 6
print(f'{b} = {bin(b)}')
# AND
print(f'{a} and {b} = {a & b} ({bin(a & b)})')
# OR
print(f'{a} or {b} = {a | b} ({bin(a | b)})')
# XOR
print(f'{a} xor {b} = {a ^ b} ({bin(a ^ b)})')

print(f'{a} >> 3 = {a >> 3} ({bin(a >> 3)})') # 5 // 2**3
print(f'{a} << 13 = {a << 13} ({bin(a << 13)})') # 5 * 2**13

print(f'not {a} = {~a} ({bin(~a)})')  #меняет все 11 на 00, все 00 на 11ю все ++ на --


# По введенным пользователем координатам двух точек вывести уравнение прямой,
# которая проходит через эти точки

print('Координаты точки A(x1, y1):')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))

print('Координаты точки B(x2, y2):')
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

print('Уравнение прямой, проходящей через эти точки:')
if x1 == x2:
    print(f'x = {x1:.2f}')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f'y = {k:.2f} * x + {b:.3f}')


# Написать программу, которая генерирует в указанном пользователем диапазоне:
#   случайное целое число,
#   случайное вещественное число,
#   случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Если надо получить случайный символ от 'a' до 'f', вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

#   случайное целое число
print('Случайное целое число')
num_start = int(input('Начало диапазона: '))
num_end = int(input('Конец диапазона: '))
# result = int(random.random() * (num_end - num_start + 1)) + num_start
result = random.randint(num_start, num_end)
print(result)

#   случайное вещественное число
print('Случайное вещественное число')
num_start = float(input('Начало диапазона: '))
num_end = float(input('Конец диапазона: '))
# result = random.random() * (num_end - num_start) + num_start
result = random.uniform(num_start, num_end)
print(round(result, 3))

#   случайный символ
print('Случайный символ')
num_start = ord(input('Начало диапазона: '))
num_end = ord(input('Конец диапазона: '))
# result = int(random.random() * (num_end - num_start + 1)) + num_start
result = random.randint(num_start, num_end)
print(chr(result))


# Пользователь вводит две буквы. Определить их порядковый номер в алфавите и рассчитать число букв между ними

first = ord(input('1-я буква: '))
second = ord(input('2-я буква (не такая, как первая): '))
first = first - ord('a') + 1
second = second - ord('a') + 1
print(f'Порядковый номер 1-й буквы = {first}, 2-й = {second}')
print(f'Число букв между введёнными: {abs(first - second) - 1}')

# длинный способ и как облегчить себе жизнь )))
list_1 = ['a', 'b', 'c']

import string   #модуль, который импортирует массивый букв (болььшие, маленькие, другие)

a = string.ascii_lowercase
print(a)

# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# print(ord('а'))
num = int(input('Номер буквы в алфавите (1-26): '))
num = ord('a') + num - 1
print(f'Это буква {chr(num)}')

# что делать с 96
FIRST_LETTER = 96
num = int(input('Номер буквы в алфавите (1-26): '))
num = FIRST_LETTER + num
print(f'Это буква {chr(num)}')

# По введенным пользователем длинам трех отрезков определить, можно ли составить из этих отрезков треугольник.
# Если да, определить, будет ли треугольник разносторонним, равнобедренным или равносторонним.

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Треугольник не существует!!!")
elif a != b and a != c and b != c:
    print("Треугольник разносторонний")
elif a == b == c:
    print("Треугольник равносторонний")
else:
    print("Треугольник равнобедренный")


# Определить, является введённый пользователем год високосным или нет

year = int(input('Введите год в формате yyyy: '))

# короткий способ
if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
    print("Обычный")
else:
    print("Високосный")
    
# длинный способ
if year % 4 != 0:
    print("Обычный")
elif year % 100 == 0:
    if year % 400 == 0:
        print("Високосный")
    else:
        print("Обычный")
else:
    print("Високосный")

# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)

print('Введите три разных числа: ')
a = int(input('1-е: '))
b = int(input('2-е: '))
c = int(input('3-е: '))

if b < a < c or c < a < b:
    print('Среднее:', a)
elif a < b < c or c < b < a:
    print('Среднее:', b)
else:
    print('Среднее:', c)


#рекурсия
def func(a, b):
    """
    func(2, 5)
    2, 3, 4, 5
    func(5, 2)
    5, 4, 3, 2
    """
    if a == b:
        return f'{a}'
    if a < b:
        return f'{a}, {func(a + 1, b)}'
    if a > b:
        return f'{a}, {func(a - 1, b)}'
print(func(20, 5))

#увеличение стека
import sys
sys.setrecursionlimit(4500)

#рекурсия. Функция Аккермана
def akk(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return akk(m - 1, 1)
    return akk(m - 1, akk(m, n - 1))

#Решето Эратосфена. Набор простых чисел. Делится на само себя и 1.
n = int(input('До какого числа просеять простые числа: '))
sieve = [i for i in range(n)]

sieve[1] = 0
for i in range(2, n):
    if sieve[i] != 0:
        j = i + i
        while j < n:
            sieve[j] = 0
            j += i
result = [i for i in sieve if i != 0]
print(result)

#Эвклид Максимально число, которое делит нацело и 1 и 2
#gcd - greatest common division
# 30   24 - исходные  # 6 - результат

def gcd_1(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b -= a
    return a

# % - остаток на деление
def gcd_2(a, b):
    if b == 0:
        return a
    return gcd_2(b, a % b)

def gcd_3(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#генерация односвязанного списка
#вывод его наоборот без переменных и циклов

from random import randint

class Queue:
    def __init__(self, data=None, next_data=None):
        self.data = data
        self.next = next_data

    def __repr__(self):
        return f'{self.data} -> {self.next}'

    @staticmethod
    def build(size=10, lower=0, upper=100):
        #автоматическая генерация односвязанного списка
        head = spam = Queue(randint(lower, upper))
        for _ in range (size - 1):
            spam.next = Queue(randint(lower, upper))
            spam = spam.next
        return head

a = Queue().build(7)
print(a)

def go(a):
    if a.next is None:
        print(a.data)
        return None
    go(a.next)
    print(a.data)

print(go(a))











