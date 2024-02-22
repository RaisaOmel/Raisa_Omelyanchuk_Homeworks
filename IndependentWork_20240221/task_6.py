#6 Вы идете в путешествие, надо подсчитать сколько у денег у каждого студента.
# Класс студен описан следующим образом:
class Grup():
    def __init__(self):
        self.spis=[]

    def add_grup(self,student_):
        self.spis.append(student_)

    def sum_grup(self):
         return sum([elem.money for elem in self.spis])
class Student():
    def __init__(self, name, money):
        self.name = name
        self.money = money

grup=Grup()
print('Выход из ввода =')
print('Введите Имя студента в группе и через пробел сумму деньг.')
for elem in iter(input,'='):
    try:
        lst=elem.split(' ')
        print(f'Принято {lst[0]} с суммой {int(lst[1])}')
        grup.add_grup(Student(lst[0],int(lst[1])))
    except:
        print('Ошибка ввод.')

print(f'Группа едет с суммой {grup.sum_grup()}')