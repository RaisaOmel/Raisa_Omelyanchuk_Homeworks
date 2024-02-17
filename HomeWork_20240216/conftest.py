### файл для 4 задачи в test_task1.py
import pytest
@pytest.fixture()
def set_up():
    print('вход в тест')
    yield
    print('выход из теста')