# Напишите программу, доказывающую или проверяющую,
#что для множества натуральных чисел выполняется равенство:
#1+2+...+n = n(n+1)/2, где n — любое натуральное число.

import cProfile
import numpy as np

# вариант 3 - через numpy

def theory(n):
    #Правая часть:
    k = n * (n + 1) / 2

    # Левая часть:
    p = np.sum(np.arange(1, n+1))
   
    return (k == p)

#cProfile.run('theory(1000000)')

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)     - 100
#        1    0.000    0.000    0.000    0.000 hw43.py:10(theory)       - 1 000
#        1    0.000    0.000    0.004    0.004 hw43.py:10(theory)       - 1 000 000



#3" "hw43.theory(100)"
#100 loops, best of 5: 19.6 usec per loop

#3" "hw43.theory(1000)"
#100 loops, best of 5: 22.4 usec per loop

#3" "hw43.theory(10000)"
#100 loops, best of 5: 32.7 usec per loop

#3" "hw43.theory(100000)"
#100 loops, best of 5: 124 usec per loop

#Вывод: сложность алгоритма, скорее, O(log(n)) .
#Библиотека отработала отлично. Скорость работы при входном параметре 10**5 почти в 2 раза выше,
# чем во 2 варианте при входном 10**3, и в 5 раз выше варианта в рекурсией при входном 10**3.
