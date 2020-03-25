# 1
def func(x,y):
    d = x / y
    return d

print(func(4,2))
# 2
def func_1(**kwargs):
   print(f'{kwargs}')

func_1(name= 'Karen', surname='Gasparyan', birth=1997, city='Moscow', email='ZeroXKiitsu@ya.ru', phone_number='+79855790356')

# 3 
def my_func(x, y,z):
    return sum(max(x,y,z))

# 4
def my_pow(x,y):
     return 1 / x ** abs(y)
    
# 5
def char_input():
i = input("Введите число").split(" ")
a = 0
while a<len(i):
    i[a] = int(i[a])
    a = a + 1
k = 0
for j in i:
        k += j
print(k)

# 6
def int_func(**kwargs):
    kwargs = input("введите текст").split(" ")
    kwargs.lower()
    return kwargs.title()

print(int_func(‘text’))
