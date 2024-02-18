import requests
from bs4 import BeautifulSoup
import lxml
import fake_useragent
def test_status(elem):
    assert elem < 300, 'Сайт не отвечает'
def test_def1(elem):
    rezalt = elem.get('Content-Type', False)
    assert rezalt != False, 'сайта ответ пришел не верный'
    assert rezalt.find('html') != -1, 'Неверный формат ответа'

def test_def2(elem):
    rezalt = elem.get('Content-Type', False)
    assert rezalt != False, 'сайта ответ пришел не верный'
    assert rezalt.find('json') != -1, 'Неверный формат ответа'

##1 GitHub тестирование соединения и результата получения
# rez = ''
# user = fake_useragent.UserAgent().random
# headers = {'user-agent': user}
# ##### получить токен и заходить нужно в 1 сессии. т.к. в каждой сессиии свой токен
# with requests.session() as session:
#     url = 'https://github.com/login'
#     try:
#         response = session.get(url, headers=headers)
#         test_status(response.status_code)
#         rez = response.text
#         head = response.headers
#         test_def1(head)
#         soup = BeautifulSoup(rez, 'lxml')
#         block = soup.find('input', {'name': 'authenticity_token'})
#         val = block.get('value')
#         print(block)
#     except AssertionError as e:
#         print(e)
##2
# user = fake_useragent.UserAgent().random
# headers = {'user-agent': user}
# url='https://httpbin.org/user-agent'
# try:
#     response=requests.get(url)
#     test_status(response.status_code)
#     head=response.headers
#     test_def2(head)
#     user1 = response.json().get('user-agent')
#
#     response = requests.get(url, headers=headers)
#     test_status(response.status_code)
#     head = response.headers
#     test_def2(head)
#     user2 = response.json().get('user-agent')
#     assert user1 == user2, f'Пользователь изменился с !!!! {user1} !!!!  на  !!!! {user2} !!!!'
# except AssertionError as e:
#     print(e)

## 3
url='https://httpbin.org/put'
user = fake_useragent.UserAgent().random
headers = {'user-agent': user}
try:
    response = requests.put(url,headers=headers)
    test_status(response.status_code)
    head = response.headers
    test_def2(head)
    print('put',head)
    print(response.json().get('headers').get('User-Agent'))
except AssertionError as e:
    print(e)

## 4
user = fake_useragent.UserAgent().random
headers = {'user-agent': user}
url='https://httpbin.org/post'
try:
    response = requests.post(url,headers=headers)
    test_status(response.status_code)
    head = response.headers
    test_def2(head)
    print('post', head)
    print(response.json().get('headers').get('User-Agent'))
except AssertionError as e:
    print(e)

## 5
user = fake_useragent.UserAgent().random
headers = {'user-agent': user}
url='https://httpbin.org/patch'
try:
    response = requests.patch(url,headers=headers)
    test_status(response.status_code)
    head = response.headers
    test_def2(head)
    print('patch', head)
    print(response.json().get('headers').get('User-Agent'))
except AssertionError as e:
    print(e)