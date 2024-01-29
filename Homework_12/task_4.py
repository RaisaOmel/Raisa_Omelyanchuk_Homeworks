#(try-except, изучить raise)
#Напишите программу, которая запрашивает ввод строки.
#Если в ней есть хотя бы символ - число, то выведите ошибку и заново попросите ввести строку.
#Если все символ буквы, то выведите количество буквы «а».

while True:
    try:
        str_ = input('введите строку ')
        kol = 0
        for letter in str_:
            if letter.isdigit():
                raise Exception('ввели цифру в строке')
            else:
                kol += 1 if letter.lower() in 'а' else 0

        print(f'строка содержит {kol} "а"')
        break
    except Exception as e:
        print(e)

