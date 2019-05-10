#Решето Эратосфена.
#Написать два алгоритма нахождения i-го по счёту простого числа.
#Функция нахождения простого числа должна принимать на вход натуральное
#и возвращать соответствующее простое число.
#Проанализировать скорость и сложность алгоритмов.

import cProfile

#SLP - Simple Element Position
#Не додумала формулу сколько простых чисел приходится на обычные
#Не нашла простое решение. Использую тупенькое.
def sieves(SLP):
    if SLP < 9500:
        n = SLP * 10
    elif SLP < 664000:
        n = SLP * 15
    else:
        n = SLP * 20

    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    result = [i for i in sieve if i != 0]
    return result[SLP - 1]
    

#cProfile.run('sieves(100000)')

#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.002    0.002 <string>:1(<module>) - 100
#        1    0.023    0.023    0.026    0.026 hw4-4.py:12(sieves) - 1000

#        1    0.175    0.175    0.210    0.210 hw4-4.py:12(sieves) - 10000
#       1    0.025    0.025    0.025    0.025 hw4-4.py:20(<listcomp>) - 10000

#        1    1.917    1.917    2.183    2.183 hw4-4.py:12(sieves)   - 100000
#        1    0.162    0.162    0.162    0.162 hw4-4.py:20(<listcomp>) - 100000



#"hw44.sieves(100)"
#100 loops, best of 5: 965 usec per loop

#4" "hw44.sieves(200)"
#100 loops, best of 5: 2 msec per loop

#4" "hw44.sieves(300)"
#100 loops, best of 5: 3.07 msec per loop

#4" "hw44.sieves(400)"
#100 loops, best of 5: 4.13 msec per loop

#4" "hw44.sieves(1000)"
#100 loops, best of 5: 10.7 msec per loop


#Вывод: Сложность алгоритма похожа на линейную O(n).
# Алгоритм проходит по 1 разу по циклу вне зависимости от величины входного параметра.
