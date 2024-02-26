from jinja2 import Template, Environment, FileSystemLoader

lst = ['Рая', 'Юля','Иван', 'Вася']

file_loader=FileSystemLoader(r'C:\Users\1\Desktop\HomeWorks\Raisa_Omelyanchuk_Homeworks\Jinja\templates')
env=Environment(loader=file_loader)
tm=env.get_template('about.html')
msg=tm.render(List_table=lst, domain="https://proproprogs.ru/", title='jinja сбор частями')
print(msg)
# about  можно написать
# {{ super() }}
# или
#{% block table_content %} {{ super() }} {% endblock content %} но не будет видно: БЛОК КОНТЕНТА перенос как super()
# но таким образом мы указываем какие блоки брать на эту страницу а какие игнорировать
# если мы вместо {{li}} используем блок то чтобы получить внешние данные (из for) нужно написать:  <li>{% block item scoped%}{{li}}{% endblock %}</li>