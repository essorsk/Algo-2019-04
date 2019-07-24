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


# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

START_NUM = 2
END_NUM = 99
START_DIV = 2
END_DIV = 9
print('вариант 1:')
for i in range(START_DIV, END_DIV + 1):
    frequency = 0
    for j in range(START_NUM, END_NUM + 1):
        if j % i == 0:
            frequency += 1
    #print(f'Числу {i} кратно {frequency} чисел')

variables = [START_NUM, END_NUM, START_DIV, END_DIV, i, j, frequency]

calc_size(variables)


#Размер переменных: 98
#Python 3.7.1 on win32


print('вариант 2:')
frequency = [0] * (END_DIV - START_DIV + 1)
for i in range(START_NUM, END_NUM + 1):
    for j in range(START_DIV, END_DIV + 1):
        if i % j == 0:
            frequency[j - START_DIV] += 1

for i, item in enumerate(frequency, start=START_DIV):
    print(f'Числу {i} кратно {item} чисел')

variables = [START_NUM, END_NUM, START_DIV, END_DIV, i, j, frequency]

calc_size(variables)

#Размер переменных: 152
#Python 3.7.1 on win32

#При добавлении третьего цикла размер переменных увеличился на 55%.
#Вывод: не надо лишний раз зацикливаться.
