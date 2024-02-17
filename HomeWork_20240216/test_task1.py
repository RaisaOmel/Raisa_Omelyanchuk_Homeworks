## 1   тест через зеленую стрелку
# def set_up():
#     print('вход в тест')
#     yield
#     print('выход из теста')
#
#
# def test_one_is_one(set_up):
#     print('хи-хи')
#     x = 1
#     y = 1
#     assert x == y, f'тест'

##2 тест через терминал командой: pytest [ключи] <имяфайла.py>
## ключи -v   инфо какие файлы запускал и результат
##       -v -s   + выводить и print()
##       -r
# class Test_class:
#
#     def test_my(self):
#         x = 1
#         y = 1
#         assert x == y, f'тест'

## 3
# import pytest
# @pytest.fixture()
# def set_up():
#     print('вход в тест')
#     yield
#     print('выход из теста')

# def test_sending_mail1(set_up):
#     print('message 1')
#
# def test_sending_mail2(set_up):
#     print('message 2')
#
# ## Выводит
# ## test_task1.py::test_sending_mail1 вход в тест
# ## message 1
# ## PASSEDвыход из теста
# ##
# ## test_task1.py::test_sending_mail2 вход в тест
# ## message 2
# ## PASSEDвыход из теста

##4 вынесение в отдельный файл conf_test.py в папку .pytest_cache

def test_sending_mail1(set_up):
    print('message 1')

def test_sending_mail2(set_up):
    print('message 2')