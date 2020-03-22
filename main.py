# 1 задание
a = [1, 1.1, "str", False, None]

for i in a:
    print(type(i))
# 2 задание
count = int(input("Введите количество элементов списка "))
a = []
i = 0
j = 0
while i < count:
    a.append(input("Введите следующее значение списка "))
    i += 1

for k in range(int(len(a) / 2)):
    a[j], a[j + 1] = a[j + 1], a[j]
    j += 2
print(a)
# 3 задание
s_list = ['зима', 'весна', 'лето', 'осень']
s_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
months = int(input("Введите месяц по номеру "))
if months == 1 or months == 12 or months == 2:
    print(s_dict.get(1))
    print(s_list[0])
elif months == 3 or months == 4 or months == 5:
    print(s_dict.get(2))
    print(s_list[1])
elif months == 6 or months == 7 or months == 8:
    print(s_dict.get(3))
    print(s_list[2])

elif months == 9 or months == 10 or months == 11:
    print(s_dict.get(4))
    print(s_list[3])
else:
    print("Такого месяца не существует")
# 4 задание
string = input("введите строку ")
word = []
numbers = 1
for i in range(string.count(' ') + 1):
    word = string.split()
    if len(str(word)) <= 10:
        print(f" {numbers} {word[i]}")
        numbers += 1
    else:
        print(f" {numbers} {word[i][0:10]}")
        numbers += 1
# 5 задание
my_list = [7, 5, 3, 3, 2]
print(my_list)
digit = int(input("Введите число"))
for i in range(len(my_list)):
    if my_list[i] == digit:
        my_list.insert(i + 1, digit)
        break
    elif my_list[0] < digit:
        my_list.insert(0, digit)
        break
    elif my_list[-1] > digit:
        my_list.append(digit)
        break
    elif my_list[i] > digit and my_list[i + 1] < digit:
        my_list.insert(i + 1, digit)
        break

print(my_list)
# 6 задание
goods = int(input("Введите количество товара "))
n = 1
my_dict = []
my_list = []
analysis = {}
while n <= goods:
    my_dict = dict({'название': input("введите название "), 'цена': input("Введите цену "),
                    'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
    my_list.append((n, my_dict))
    n += 1
    analysis = dict(
        {'название': my_dict.get('название'), 'цена': my_dict.get('цена'), 'количество': my_dict.get('количество'),
         'ед': my_dict.get('ед')})
print(my_list)
print(analysis)
