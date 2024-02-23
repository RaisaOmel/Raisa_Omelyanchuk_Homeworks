# 7
"""Создайте класс Students, содержащий поля: фамилия и инициалы, номер группы,
успеваемость (список из пяти элементов).
Создать класс School:
Добавить возможно для добавления студентов в школу
Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 5 или 6.
Добавить возможность вывода учеников заданной группы
Добавить возможность вывода учеников претендующих на автомат(средний балл >= 7)
"""

class School:
    def __init__(self,name):
        self.name=name
        self.students=[]

    def add_studet(self,student):
        self.students.append(student)

    def del_studet(self,student):
        if self.students.count(student)>0:
            self.students.remove(student)

    def info_assessment(self,assessment):
        print(f'студенты имеющие оценки: {assessment}')
        for student_ in self.students:
            if len([elem for elem in student_.assessment if elem in assessment])==5:
                print(f'{student_.name}: {student_.assessment}')
    def info_avtomat(self,assessment):
        print(f'студенты имеющие среднюю оценки более или равно {assessment}:')
        for student_ in self.students:
            if sum([elem for elem in student_.assessment])/5>=assessment:
                print(f'{student_.name}: {student_.assessment}')

    def info_grup(self,group):
        print(f'студенты из группы {group.name}:')
        for elem in self.students:
            if elem.group==group:
                print(f'{elem.name}: {elem.assessment}')

class Group:
    def __init__(self, name,school):
        self.name=name
        self.school=school

class Students:
    def __init__(self,name, group,assessment):
        self.name=name
        self.group=group
        self.assessment=assessment
        group.school.add_studet(self)

school=School("Курсы")
group1=Group('def_17',school)
group2=Group('def_18',school)
student1=Students('Омел Р.Н.', group1,[6,7,7,6,7])
student2=Students('Туктук Я.Я.', group1,[9,5,10,8,7])
student3=Students('Нетуктук Я.Я.', group2,[3,5,6,3,2])
school.info_grup(group1)
print('-----')
school.info_assessment((6,7))
print('-----')
school.info_avtomat(7)




