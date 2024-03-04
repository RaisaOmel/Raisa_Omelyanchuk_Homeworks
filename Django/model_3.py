'''Создайте Django приложение для управления информацией о курсах и студентах в учебном заведении.
 Вам необходимо создать модели данных для курсов, студентов, преподавателей и их оценок.
 Каждый курс должен иметь одного преподавателя, и каждый студент может быть записан на несколько курсов.
 Модели данных должны включать следующие поля:

Модель "Teacher" (Преподаватель):
Имя (first_name) - строка, максимальная длина 100 символов.
Фамилия (last_name) - строка, максимальная длина 100 символов.
Должность (position) - строка, максимальная длина 100 символов.

Модель "Course" (Курс):
Название (title) - строка, максимальная длина 200 символов.
Преподаватель (teacher) - внешний ключ к модели "Teacher".
Дата начала (start_date) - дата начала курса.

Модель "Student" (Студент):
Имя (first_name) - строка, максимальная длина 100 символов.
Фамилия (last_name) - строка, максимальная длина 100 символов.
Курсы (courses) - поле, связывающее студента с курсами.

Модель "Grade" (Оценка):
Курс (course) - поле связанное с  "Course".
Студент (student) - поле связанное с "Student".
Оценка (grade) - поле для хранения оценки, например, от 2 до 5.'''

from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Course(models.Model):
    title = models.CharField(max_length=200, blank=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    start_date = models.DateField(null=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Grade(models.Model):
    class Point(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    grade = models.IntegerField(choices=Point.choices)

    def __str__(self):
        return f'{self.course} + {self.student}: {self.grade}'
