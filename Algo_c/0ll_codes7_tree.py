from binarytree import tree, bst, Node

#Создали класс дерева
class MyNode:
    def __init__(self, value, left=None, right=None, data=Node):
        self.value = value
        self.left = left
        self.right = right

#дерево из модуля
a = tree(height=3, is_perfect=True)
print(a)
# binary дерево из модуля
b = bst(height=3, is_perfect=True)
print(b)

#manual tree
root = Node(8)
root.left = Node(5)
root.right = Node(25)
root.left.right = Node(7)
root.right.right = Node(100)
print(root)

# Функция поиска числа и вывода пути.
print('*' * 50)
bt = bst(height=5, is_perfect=False)
print(bt)
num = int(input('Число для поиска: '))

# Функция  рекурсивного поиска
def search(bin_tree, number, path=''):
    if bin_tree.value == number:
        return f'Число {number} обнаружено по следующему пути:\nКорень{path}'
    if number < bin_tree.value and bin_tree.left is not None:
        return search(bin_tree.left, number, path=f'{path}\nШаг влево')
    if number > bin_tree.value and bin_tree.right is not None:
        return search(bin_tree.right, number, path=f'{path}\nШаг вправо')

    return f'Число {number} не обнаружено'


print(search(bt, num))


h_list = [None] * 26

#Simple hash

def my_append(value):
    my_hash = ord(value[0]) - ord('a')
    h_list[my_hash] = value
    print(h_list)

a = 'apple'
my_append(a)

b = 'banana'
my_append(b)

c = 'apricot'
my_append(c)

#Позиционная система исчисления
print(4567 == 4*10**3 + 5*10**2 + 6*10**1 + 7*10**0)

def my_index(value):
    letter = 26
    index = 0
    size = 10000

    for i, char in enumerate(value):
        index += (ord(char) - ord('a') + 1) * letter ** i

    return index % size


print(my_index(a))
print(my_index(b))
print(my_index(c))

import hashlib

print(hash('dgsdgsd'))  # 2945860525894210334
print(hash('dgsdgsd'))  # 2945860525894210334
print(hash('dgsdgsd'))  # 2945860525894210334
print(hash('dgsdgsd'))  # 2945860525894210334
print(hash('dgsdgsd'))  # 2945860525894210334

def rabin_karp(s, subs):
    '''
    поиск подстроки в строке
    '''
    len_sub = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()
    print(h_subs)   # 356a192b7913b04c54574d18c28d46e6395428ab
    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():
            #if subs == s[i:i + len_sub]:  - для всей подстроки
            return i


s = input('Введите строку: ')
subs = input('Введите подстроку: ')
print(rabin_karp(s, subs))

import hashlib
import hmac

print(hashlib.sha1('Hello'.encode('utf-8')).hexdigest())
print(hashlib.sha1('Hello.'.encode('utf-8')).hexdigest())
print(hashlib.sha1(b'ewsfqgegsgew' + 'Hello.'.encode('utf-8')).hexdigest())

print(hmac.new(key=b'giosafewiugbewiu', msg=b'Hello', digestmod=hashlib.sha1).hexdigest())



