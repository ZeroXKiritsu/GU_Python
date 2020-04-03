import json
# 1
with open('test.txt', 'w') as my_file:
    line = input('Введите текст \n')
    my_file.writelines(line)
    if not line:
        break
    content = my_file.readlines()
    print(content)
    
# 2
with open('test.txt', 'r') as my_file:
    for i in my_file.readlines():
        print(f'Количестов строк {i}')
     for j in my_file.read():
        print(f'Количестов слов {j}')

# 3 
 with open('test.txt', 'r') as my_file:
   oklad = []
   sred = []
   my_list = my_file.read().split('\n')
   for i in my_list:
         i = i.split()
            if int(i[1]) < 20000:
                sred.append(i[0])
     oklad.append(i[1])
print(f'Оклад меньше 20.000 {sred}, средний оклад {sum(map(int, oklad)) / len(oklad)}')

# 4 
my_dict = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('test.txt', 'r') as my_file:
     for i in my_file:
        i = i.split(' ', 1)
        new_file.append(my_dict[i[0]] + '  ' + i[1])
    print(new_file)
 
with open('test_2.txt', 'w') as my_file:
    my_file.writelines(new_file)

# 5
def summary():
    try:
        with open('test.txt', 'w+') as my_file:
            line = input('Введите цифры через пробел \n')
            my_file.writelines(line)
            my_number = line.split()

            print(sum(map(int, my_number)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()

# 6 
sub = {}
with open('test.txt', 'r') as my_file:
    for line in my_file:
        subject, lecture, practice, lab = line.split()
        sub[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {sub}')
    
 # 7 
profit = {}
j = {}
proove = 0
average = 0
i = 0
with open('test.txt', 'r') as my_file:
    for line in my_file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            proove = proove + profit.setdefault(name)
            i += 1
    if i != 0:
        average = proove / i
        print(f'Прибыль средняя - {average:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    j = {'средняя прибыль': round(average)}
    profit.update(j)
    print(f'Прибыль каждой компании - {profit}')

with open('test.json', 'w') as my_js:
    json.dump(profit, my_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}') 
