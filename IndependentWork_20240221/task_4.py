#4
"""Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age.
По умолчанию name = Ivan, age = 18, groupNumber = 10A.
Необходимо создать пять методов: getName, getAge, getGroupNumber, setNameAge, setGroupNumber.
Метод getName нужен для получения данных об имени конкретного студента,
метод getAge нужен для получения данных о возрасте конкретного студента,
vетод setGroupNumber нужен для получения данных о номере группы конкретного студента.
Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию,
метод setGroupNumber позволяет изменить номер группы установленный по умолчанию.
В программе необходимо создать пять экземпляров класса Student,
установить им разные имена, возраст и номер группы."""

class Student():
    def __init__(self, name='Ivan', group='10A', age=18):
        self.__name = name
        self.__groupNumber = group
        self.__age = age

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def setGroupNumber(self):
        return self.__groupNumber

    def SetNameAge(self, name, age):
        self.__name = name
        self.__age = age

    def setGroupNumber(self, group):
        self.__groupNumber = group


student1 = Student()
student1.SetNameAge('Рая', 55)
student1.setGroupNumber('dev_17')

student2 = Student()
student2.SetNameAge('Иван', 35)
student2.setGroupNumber('dev_17A')

student3 = Student()
student3.SetNameAge('Натан', 20)
student3.setGroupNumber('dev_17Б')

student4 = Student()
student4.SetNameAge('Скучно', 18)
student4.setGroupNumber('dev_17В')

student5 = Student()
student5.SetNameAge('Неинтересно', 27)
student5.setGroupNumber('dev_17С')
