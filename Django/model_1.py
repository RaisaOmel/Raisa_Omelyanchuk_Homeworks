#задание по рисунку

from django.db import models

class Subjects(models.Model):
    subject_name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.subject_name

class Students(models.Model):
    first_name = models.CharField(max_length=25, blank=False)
    last_name = models.CharField(max_length=40, blank=True)
    course = models.PositiveSmallIntegerField(default=1)
    # Если класс определен выше можно указывать без кавычек   Subjects
    favourite_subject = models.ForeignKey(Subjects,on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Teachers(models.Model):
    first_name = models.CharField(max_length=25, blank=False)
    last_name = models.CharField(max_length=40, blank=True)
    available_Hours = models.CharField(max_length=50, blank=True)
    # Если класс определен выше можно указывать без кавычек   Subjects
    subject = models.ForeignKey(Subjects, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Exams(models.Model):
    exam_date = models.DateField()
    exam_points = models.PositiveSmallIntegerField()
    # Если класс определен выше можно указывать без кавычек  Students  и  Teachers
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teachers, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.teacher} + {self.student}: {self.exam_points}'