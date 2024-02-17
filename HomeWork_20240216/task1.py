##1
# #Написать функцию, которая будет заполнять список степенями числа 2 (от 2^1 до 2^n). n - целое число.
def my_fun(n, lst=[]):
    return [2 ** elem for elem in range(n + 1)]


n = input('введите число ')
assert n.isdigit(), ""

print(my_fun(int(n)))

# 2
"""Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
Чтобы получить список ключей - использовать метод .keys()"""

dct = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
dct1 = {key + str(len(key)): dct[key] for key in dct.keys()}
print(dct1)
for key in dct1.keys():
    assert key[-1].isdigit(), 'не цифра последний символ'

# 3
"""Ввести строку. Если длина строки больше 10 то создать новую строку с 3 восклицательными
знаками и
вывести на экран. Если у нас меньше чем 10 то вывести второй символ строки"""

string = input('введите строку ')
assert len(string) != 10, 'длина строки 10 символов и что делать не знаем'
if len(string) < 10:
    print(string[1])
elif len(string) > 10:
    print(string + '!!!')

# 4
# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры
n = input('введите число ')
assert n.isdecimal(), "ввели не число"
dct = {kol: {'name': input('введите имя '), 'email': input('введите email ')} for kol in range(int(n) + 1)}
print(dct)


# 5
# Напишите программу, которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a;b], которые кратны числу 3.
# В приведенном ниже примере среднее арифметическое считается для чисел на отрезке [−5;12].
# Всего чисел, делящихся на 3, на этом отрезке 6: − 3 , 0 , 3 , 6 , 9 , 12.
# Их среднее арифметическое равно 4.5.

def my_fun(a, b):
    lst = [elem for elem in range(a, b + 1) if elem % 3 == 0]
    print(lst)
    return sum(lst) / len(lst)


a = input('введите число ')
a1 = a[:]
if a[0] == '-':
    a1 = a[1:]
assert a1.isdecimal(), "ввели не число"
b = input('введите число ')
b1 = b[:]
if b[0] == '-':
    b1 = b[1:]
assert b1.isdecimal(), "ввели не число"
a = int(a)
b = int(b)
if a > b:
    a, b = b, a

print(my_fun(a, b))
