#7.	В одномерном массиве целых чисел определить
#два наименьших элемента. Они могут быть как равны между собой
#(оба являться минимальными), так и различаться.

import random

array = [random.randint(0, 100) for _ in range(10)]
print(array)

m0, m1 = 0, 0

if array[0] < array[1]:
    m0 = array[0]
    m1  = array[1]
else:
    m0 = array[1]
    m1 = array[0]
    
for i in range(2, len(array)):
    if array[i] <= m0:
        m1 = m0
        m0 = array[i]
        
    elif array[i] < m1:
        m1 = array[i]
        
print(f'Минимальные элементы данного массива: {m0}, {m1}')
