#Напишите программу, доказывающую или проверяющую,
#что для множества натуральных чисел выполняется равенство:
#1+2+...+n = n(n+1)/2, где n — любое натуральное число.

import cProfile

# вариант 1 - рекурсия.

def recurs(n):
    if n == 1:
        return n
    sums = n + recurs(n-1)
    return sums

def theory(n):
    #Правая часть:
    k = n * (n + 1) / 2

    # Левая часть:
    p = recurs(n)

    return (k == p)

#print(theory(10))
#cProfile.run('theory(1000)')

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      10/1    0.000    0.000    0.000    0.000 hw41.py:9(recurs)       - 10
#       50/1    0.000    0.000    0.000    0.000 hw41.py:9(recurs)      - 50
#      100/1    0.000    0.000    0.000    0.000 hw41.py:9(recurs     - 100
#     987/1    0.003    0.000    0.003    0.003 hw41.py:9(recurs)       - 1000 + Error



#1" "hw41.theory(10)"
#100 loops, best of 5: 5.42 usec per loop

#1" "hw41.theory(50)"
#100 loops, best of 5: 24.8 usec per loop

#1" "hw41.theory(100)"
#100 loops, best of 5: 49.3 usec per loop

#1" "hw41.theory(900)"
#100 loops, best of 5: 524 usec per loop

#Вывод: сложность алгоритма O(n).
#При увеличении входного параметра кратно увеличивается количество вызовов рекурсивной функции.
#Время работы алгоритма так же увеличивается линейно.
#Ограничение использования - количество стеков (до 987 без расширения)

