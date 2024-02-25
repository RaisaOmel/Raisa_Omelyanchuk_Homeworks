from jinja2 import Template, Environment, FileSystemLoader

persons = [{'name': 'Рая', 'old': 55,'weigth':86.3},
           {'name': 'Иван', 'old': 35,'weigth':78.2},
           ]

# # папка где лежат шаблоны
# #file_loader=FileSystemLoader('templates')
# #file_loader=FileSystemLoader('') усли не в папке а там же
# file_loader=FileSystemLoader(r'C:\Users\1\Desktop\HomeWorks\Raisa_Omelyanchuk_Homeworks\Jinja\templates')
# env=Environment(loader=file_loader)
# tm=env.get_template('jinja2.html')
# msg=tm.render(users=persons)
# print(msg)

# если заглавие и подвал на всех страницах сайта один, а меняется тело
file_loader=FileSystemLoader(r'C:\Users\1\Desktop\HomeWorks\Raisa_Omelyanchuk_Homeworks\Jinja\templates')
env=Environment(loader=file_loader)
tm=env.get_template('page.html')
msg=tm.render(users=persons, domain="https://proproprogs.ru/", title='jinja сбор частями')
print(msg)
# если нужно исключить ошибку (не найден файл) прописываем в html файле ignore missing
# можно подключать несколько шаблонов: {% include ['page1.html','page2.html'] ignore missing %}

#импортировать можно нескольками вариантами:
#{% import 'dialogs.html' as dlg %}
# с вызовом {{ dlg.dialog_1('внимание','это текстовый документ') }}
# или
#{% from 'dialogs.html' import dialog_1 as dlg %}
" с вызовом {{ dlg('внимание','это текстовый документ') }}"