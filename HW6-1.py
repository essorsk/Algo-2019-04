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


#Размер переменных: 40
#Python 3.7.1 on win32

#Размер переменных не изменился, вводила ли я число в 2 знака или 600 знаков
