#Написать программу сложения и умножения двух шестнадцатеричных чисел.
#При этом каждое число представляется как массив, элементы которого —
#цифры числа. Например, пользователь ввёл A2 и C4F.
#Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
#Сумма чисел из примера:
#[‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import Counter
from collections import deque
TPL = deque(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'])

a = deque(input('Input 1st number 16-format (0-9 & A-F): '))
b = deque(input('Input 2nd number 16-format (0-9 & A-F): '))
#a = deque(['A', '2'])
#b = deque(['C', 'F'])
s = deque()
#p = deque()

m = int(min(len(a), len(b)))
n = 0
k = 0
#Add

for i in range(m):
   n = TPL.index(a[i]) + TPL.index(b[i]) + k
   k = 0
   if n <= len(TPL):
       s.appendleft(TPL[n])
   else:
        s.appendleft(TPL[n - len(TPL)])
        k = 1
if k == 1:
    s.appendleft(TPL[1])
    print(s)
else:
    print(s)
    
        
    
    
    
