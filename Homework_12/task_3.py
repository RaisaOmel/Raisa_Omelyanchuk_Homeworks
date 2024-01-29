#В текстовом файле посчитать количество строк,
#а также для каждой отдельной строки определить количество в ней символов.
kol=0
smv=0
with open('file2.txt','r') as file:
    for num, line in enumerate(file,1):
        lst=[1 for let in line if let.isalpha()]
        smv+=len(lst)
        kol=num
        print(f'{num}. символов={len(lst)} в строке "{line[:-1]}"')

print(f'в файле {kol} строк и {smv} символов')