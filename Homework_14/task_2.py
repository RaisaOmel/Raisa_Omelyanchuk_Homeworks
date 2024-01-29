#Случайным образом генерируется список из чисел.
# Создайте функцию, которая посчитает сумму элементов.
from random import random as rd
def summ(elem):
    lst=[ int(rd()*100)  for _ in range(elem)]
    print(lst)
    return sum(lst)

print(summ(int(input('количество случайных чисел '))))