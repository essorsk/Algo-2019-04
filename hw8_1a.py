#1) Определение количества различных подстрок с использованием хеш-функции.
#Пусть на вход функции дана строка.
#Требуется вернуть количество различных подстрок в этой строке.


import hashlib

def subs(s):

    a = []
    for i in range(1, len(s) + 1):
        for j in range(1,len(s)):
            p = s[(i - 1):(i + j - 1)]
            h = (hashlib.sha1(p.encode('utf-8')).hexdigest())
            if h in a:
                pass
            else:
                a.append(h)

    print(len(a))

subs('sova')
