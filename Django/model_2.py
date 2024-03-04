'''Создайте Django приложение для управления информацией о книгах в библиотеке.
 Вам необходимо создать модели данных для книг, авторов и категорий книг.
Каждая книга должна быть связана с одним автором и одной категорией.
Модели должны включать следующие поля:

Модель "Author" (Автор):
Имя (first_name) - строка, максимальная длина 100 символов.
Фамилия (last_name) - строка, максимальная длина 100 символов.
Дата рождения (birth_date) - дата рождения автора.

Модель "Category" (Категория):
Название (name) - строка, максимальная длина 100 символов.

Модель "Book" (Книга):
Название (title) - строка, максимальная длина 200 символов.
Описание (description) - текстовое поле для описания книги.
Год издания (publication_year) - целое число.
Автор (author) - внешний ключ к модели "Author".
Категория (category) - внешний ключ к модели "Category".'''

from django.db import models
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Book(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=False)
    publication_year = models.PositiveSmallIntegerField(default=2024)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)


    def __str__(self):
        return self.title