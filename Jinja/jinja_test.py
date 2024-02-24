from jinja2 import Template, Environment, FileSystemLoader   #, escape
#### 1 способ
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#
# person = Person('Рая', 55)
# tm = Template('мне {{p.age}}. Зовут {{p.name}}')
# # или так
# tm = Template('мне {{p.age}}. Зовут {{p.get_name()}}')
# msg = tm.render(p=person)
#
# #### 2способ
# per = {'name': 'Рая', 'age': 55}
# tm = Template('мне {{p["age"]}}. Зовут {{p.name}}')
# msg = tm.render(p=per)
#
# #### 3способ
# #{%raw%}.......{%endraw%} -это спецификатор шаблона. передается без изменения
# data='''{%raw%}
# Модуль многострочный
#  с подстановкой {{name}}
#  {%endraw%}'''
# tm = Template(data)
# name='Рая'
# msg = tm.render(name=name)
# # print(msg)
#
# #### 4способ
# # если хотим текст, а не ссылку в HTML документе нужно экронировать < > /      e - экронирование
# link='''В HTML-документе ссылки определяются так: <a href="#">ссылка</a>'''
# tm = Template('{{ link | e}}')
# msg = tm.render(link=link)
# #print(msg)
# #получим
# # В HTML-документе ссылки определяются так: &lt;a href=&#34;#&#34;&gt;ссылка&lt;/a&gt;
# #или
# # msg=escape(link)
# # print(msg)
#
# #### 1 способ в нtml
# cities=[{'id':0, 'city':'Курск'},
#         {'id':1, 'city':'Москва'},
#         {'id':2, 'city':'Минск'}]
# link='''<select name = "cities">
# {%- for c in cities -%}
# {% if c.id>1 -%}
# <option value="{{c['id']}}">{% filter upper %}{{c['city']}}{% endfilter %}</option>
#
# {% elif c.city=="Москва" -%}
# {{c['city']}}
# {% else %}
# <option>{{c['city']}}</option>
# {% endif -%}
# {% endfor -%}
# </select>'''
# tm = Template(link)
# msg = tm.render(cities=cities)
# print(msg)
# #получили
# #<select name = "cities">
# #<option>Курск</option>
# #Москва
# #<option value="2">МИНСК</option>
# #</select>

# #### способ в нtml   sum(iterable, attribute=None, start=0) - вычисление суммы поля коллекции
# cars=[{'model':'Ауди', 'price': 23000},
# {'model':'Шкода', 'price': 17300},
# {'model':'Вольво', 'price': 44300},
# {'model':'Audy', 'price': 23000},
# {'model':'фольцваген', 'price': 21300},
# ]
# tpl='Суммарная стоимость всех авто {{ cs | sum(attribute="price")}}'
# tm = Template(tpl)
# msg = tm.render(cs=cars)
# print(msg)
#### 2способ: max  min random(случайные выбор) replace
# cars=[{'model':'Ауди', 'price': 23000},
# {'model':'Шкода', 'price': 17300},
# {'model':'Вольво', 'price': 44300},
# {'model':'Audy', 'price': 23000},
# {'model':'фольцваген', 'price': 21300},
# ]
# #tpl='Максимальная стоимость у {{ (cs | max(attribute="price")).model}}'
# #tpl='Максимальная стоимость у {{ (cs | random).model}}'
# tpl='Список с заменой {{ cs | replace("А","Я")}}'
# tm = Template(tpl)
# msg = tm.render(cs=cars)
# print(msg)

# #### 3способ
# lst=[1, 2, 3, 4, 5, 6]
# tpl='Суммарная стоимость всех авто {{ cs | sum}}'
# tm = Template(tpl)
# msg = tm.render(cs=lst)
# print(msg)

# #### 4способ макроопределение
# html='''
# {%- macro input(name, value='', type='text', size=20) -%}
# <input type="{{ type }}" name="{{ name }}" value="{{ value }}" size="{{ size}}">
# {%- endmacro -%}
#
# <p>{{ input('username') }}
# <p>{{ input('email') }}
# <p>{{ input('password') }}
# '''
# tp=Template(html)
# msg=tp.render()
# print(msg)

# #### 5 способ call пример: вложеный список в список
# persons = [{'name': 'Рая', 'old': 55,'weigth':86.3},
#            {'name': 'Иван', 'old': 35,'weigth':78.2},
#            ]
# html='''
# {%- macro list_users(list_of_user) -%}
# <ul>
# {% for u in list_of_user -%}
#     <li>{{u.name}}
# {% endfor -%}
# </ul>
# {% endmacro %}
#
# {{list_users(users)}}
# '''
# tp=Template(html)
# msg=tp.render(users=persons)
# print(msg)
# # Результат
# #<ul>
# #<li>Рая
# #<li>Иван
# #</ul>
#
# # еще вариант
#
# persons = [{'name': 'Рая', 'old': 55,'weight':86.3},
#            {'name': 'Иван', 'old': 35,'weight':78.2},
#            ]
#
# html='''
# {%- macro list_users(list_of_user) -%}
# <ul>
#     {% for u in list_of_user -%}
#         <li>{{u.name}} {{caller(u)}}
#     {% endfor -%}
# </ul>
# {% endmacro %}
#
# {% call(user) list_users(users) %}
#     <ul>
#         <li>age: {{user.old}}
#         <li>weight: {{user.weight}}
#     </ul>
# {%- endcall -%}
# '''
# tp=Template(html)
# msg=tp.render(users=persons)
# print(msg)
#
# #Результат
# #<ul>
# #    <li>Рая
# #    <ul>
# #        <li>age: 55
# #        <li>weight: 86.3
# #    </ul>
# #    <li>Иван
# #    <ul>
# #        <li>age: 35
# #        <li>weight: 78.2
# #    </ul>
# #    </ul>