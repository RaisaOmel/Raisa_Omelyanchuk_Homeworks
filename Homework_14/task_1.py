#Вводится год с клавиатуры. Создайте функцию, которая будет
# проверять, является ли год високосным.
godik = int(input('введите год '))
print(godik ,'высокостный' if godik%4==0 and (godik%400==0 or godik%100!=0) else 'невысокостный')

