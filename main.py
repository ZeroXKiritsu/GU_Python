# 1
from sys import argv
from functools import reduce
from itertools import count
from itertools import cycle
from math import factorial

def cash():
    script_name,hours,cash,premiya = argv
    pay = hours * cash
    return pay + premiya

print(f'Размер заработной платы составил: {cash()}')

# 2
def greater():
    a = input().split()
    for i in range(len(a)-1):
        n = int(a[i])
        i += 1
         m = list(int(a[i]))
         if m > n:
            n = m
            print(m, end=' ')
            
# 3
print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')
# 4
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [el for el in my_list if my_list.count(el) < 2]
print(new_list)
# 5
def gen(el_p, el):
    return el_p * el

print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

# 6
for el in count(int(input('Введите стартовое число '))):
    print(el)
    
my_list = [True, 'ABC', 123, None,6.6]
for el in cycle(my_list):
    print(el)
    
# 7 
def generator():
    for el in count(1):
        yield factorial(el)
        
 gen = generator()

x = 0
for i in gen:
    if x < 15:
        print(i)
        x += 1
    else:
        break 
    
