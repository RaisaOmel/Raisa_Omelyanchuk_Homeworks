#Имеется текстовый файл prices.txt с информацией о заказе из интернет магазина.
# В нем каждая строка с помощью символа табуляции \t разделена на три колонки:
# наименование товара; количество товара (целое число); цена (в рублях) товара за 1 шт. (целое число).
# Напишите программу, подсчитывающую общую стоимость заказа.
lst=[]
try:
    with open('price.txt','r', encoding='windows-1251') as file:
        lst=file.readlines()
except:
    print('ошибка с работой файла')

zakaz=sum(list(int(line.split('\t')[1])*int(line.split('\t')[2]) for line in lst))
print(f"Сумма заказа {zakaz}")