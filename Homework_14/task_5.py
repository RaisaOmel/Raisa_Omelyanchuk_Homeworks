#Дано натуральное число N.
# Выведите слово YES, если число N является точной степенью двойки,
# или слово NO в противном случае (использовать рекурсивную функцию)
def fun(num):
    if num == 1:
        return 1
    elif round(num,0) != num:
        return 0
    else:
        return fun(num/2)

print('YES' if fun(int(input('введите натуральное число '))) ==1 else 'NO')

