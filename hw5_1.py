#Пользователь вводит данные о количестве предприятий,
#их наименования и прибыль за 4 квартал (т.е. 4 числа)
#для каждого предприятия. Программа должна определить среднюю прибыль
#(за год для всех предприятий) и отдельно вывести наименования предприятий,
#чья прибыль выше среднего и ниже среднего.

from collections import Counter
from collections import namedtuple

enterprise = []
n = int(input('Number of ventures is: '))
s = 0
#Сохранила в кортеже все кварталы, для данной задачи, в кортеже можно было
#оставить только название и сумму за год (FY)
Venture = namedtuple('Venture', 'vname, Q1, Q2, Q3, Q4, FY')
for i in range(n):
    ename = input(str(i + 1) + ' venture name: ')
    q1 = float(input('Q1 profit: '))
    q2 = float(input('Q2 profit: '))
    q3 = float(input('Q3 profit: '))
    q4 = float(input('Q4 profit: '))
    fy = (q1 + q2 + q3 + q4)
    ename = Venture(ename, q1, q2, q3, q4, fy)
    enterprise.append(ename)
#    print(ename)
    s += fy

avp = s / n
print(f' Average profit for all ventures is: {avp:.2f}')
#print(enterprise)

print('Ventures with profit above average are: ')
for i in enterprise:
    if i.FY > avp:
        print(i.vname)

print('Ventures with profit below average are: ')
for i in enterprise:
    if i.FY < avp:
       print(i.vname)
