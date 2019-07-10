
from collections import Counter
# Создание пустого списка
a = Counter()
# посчитает сколько букв. выведет в порядке убывания количества
b = Counter('barakadabra')
# 2 варианта создания словаря
c = Counter({'cats': 7, 'dog': 3})
d = Counter(cats=7, dogs=3)
print(a, b, c, d, sep='\n')

# Выведет, что 0 элементов, присвоит 3 и выведет 3
print(b['z'])
b['z'] = 3
print(b)

#Выведет 3 наиболее часто встречающихся
print(b.most_common(3))
#выведет буквы одинаковые вместе в том порядке, что встречаются впервые
print(list(b.elements()))

# Можно делать математические операции + - и прочие
e = Counter(a=2, b=-3, c=1)
f = Counter(a=1, b=2, c=2)
print(e, f, sep='\n')
print(e + f)
print(e - f)
print(e & f)
print(e | f)


from collections import defaultdict
#Создание пустого словаря
a = defaultdict()
print(a)
#Можно со строками делать то же, что и со словарями
s = 'dvbedhiveiwfbqwosfbdsaivbwdsifbsivbweiuvbewubvwiuvbqwuvbwriovbrwifubvrivbwri'
b = defaultdict(int)
# Посчитает и вставит в словарь кол-во букв
for char in s:
    b[char] += 1
print(b)
#Можно из списка вывести на каком расстоянии бегают животные
list_1 = [('cat', 1), ('dog', 2), ('cat', 2), ('dog', 4), ('cat', 3), ('dog', 5), ]
c = defaultdict(list)
#Для списка используется аппенд для добавления
for key, value in list_1:
    c[key].append(value)
print(c)
#Если множество, то используется адд
list_1 = [('cat', 1), ('dog', 2), ('cat', 2), ('dog', 4), ('cat', 1), ('dog', 5), ]
c = defaultdict(set)

for key, value in list_1:
    c[key].add(value)
print(c)

#Можно добавить функцию автоопределения в словаре
d = defaultdict(lambda: 'unknown')
d.update(rex='dog', markiz='cat')
print(d)
#Выведет, что собака
print(d['rex'])
#Выведет, что "неизвестный"
print(d['barsik'])

#Работа с очередями
from collections import deque

#пустая очередь
a = deque()
b = deque([1, 2, 3, 4])
#преобразует строки в список. выведет deque(['a', 'b', 'r', 'a', 
c = deque('abraladabra')
print(a, b, c, sep='\n')

#ставит 3 последних элемента
d = deque([1, 2, 3, 4, 5], maxlen=3)
print(d)

print('*' * 50)
#создаст автоматически от 0 до 4 
e = deque([i for i in range(5)], maxlen=7)
print(e)
# в конец или в начало добавит элемент
e.append(5)
print(e)
e.appendleft(6)
print(e)
# расширит список в конец, но с ограничением, заданном раньше
e.extend([7, 8])
print(e)
#расширит список с начала. Вначале добавит 9, потом 10 на 1 место
e.extendleft([9, 10])
print(e)
#выведет и удалит элемент из конца / начала
print(e.pop())
print(e)
print(e.popleft())
print(e)

#перевернет строку
e.reverse()
print(e)
#2 элемента из конца переставит по 1 вначало - 2 шт. И наоборот - 3 шт
e.rotate(2)
print(e)
e.rotate(-3)
print(e)


from collections import OrderedDict

# python 3.7 dict == OrderedDict

from collections import namedtuple

hero_1 = ('Ivan', 'kri', 100, 0, 250)
print(hero_1[4])


class Person:

    def __init__(self, name, race, health, mana, armor):
        self.armor = armor
        self.mana = mana
        self.race = race
        self.name = name
        self.health = health

    def __repr__(self):
        return 'Это я'

hero_2 = Person('Ivan', 'kri', 100, 0, 250)
print(hero_2.armor)
print(hero_2)

#Имя до = должно совпадать с тем, что в ()
New_Person_123 = namedtuple('New_Person_123', 'name, race, health, mana, armor')
hero_3 = New_Person_123('Ivan', 'kri', 100, 0, 250)
#Выведет элемент, весь список героя
print(hero_3.armor)
print(hero_3)

print('*' * 50)
Point = namedtuple('Point', 'x y z')
#Можно создать кортеж с заданными значениями по умолчанию
# Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
p1 = Point(2, z=4, y=3)
print(p1)

print(p1.x)
# p1.x = 22 - так не работает замещение
#Так делается замещение элемента
p1 = p1._replace(x=22)
print(p1)
#Выведет кортеж как словарь
print(dict(p1._asdict()))
#Выведет, какие поля в кортеже
print(p1._fields)





