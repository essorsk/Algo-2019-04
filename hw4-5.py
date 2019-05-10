#Написать два алгоритма нахождения i-го по счёту простого числа.
#Функция нахождения простого числа должна принимать на вход натуральное
#и возвращать соответствующее простое число.
#Проанализировать скорость и сложность алгоритмов.

import cProfile

#SLP - Simple Element Position

def primes(SLP):
    if SLP < 9500:
        n = SLP * 10
    elif SLP < 664000:
        n = SLP * 15
    else:
        n = SLP * 20

    START = 2
    prime = []
    k = 0
    for i in range(START, n):
        for j in range(2, i):
            if i % j == 0:
                k = k + 1
        if k == 0:
            prime.append(i)
        else:
            k = 0
                    
    return prime[SLP - 1]
    

#cProfile.run('primes(500)')


#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.093    0.093    0.094    0.094 hw45.py:11(primes)               - 100
#      168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects - 100

#        1    2.364    2.364    2.364    2.364 hw45.py:10(primes)               - 500
#      669    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects} - 500

#        1    9.703    9.703    9.703    9.703 hw45.py:10(primes)               - 1000
#     1229    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects} - 1000


#5" "hw45.primes(10)"
#100 loops, best of 5: 668 usec per loop

#5" "hw45.primes(20)"
#100 loops, best of 5: 2.53 msec per loop

#5" "hw45.primes(50)"
#100 loops, best of 5: 16.7 msec per loop

#5" "hw45.primes(100)"
#100 loops, best of 5: 77.6 msec per loop

#Сложность алгоритма ближе к квадратной зависимости O(n*n).
#С увеличением входного параметра, почти линейно увеличивается количество циклов.
#Классическая реализация затратнее Решета Эратосфена.



