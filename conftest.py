import pytest


@pytest.fixture(scope="function")
def set_up():
   print("Вход в систему выполнен")
   yield
   print("Произведен выход из системы")


@pytest.fixture(scope="module")
def some():
   print("Начало")
   yield
   print("Конец")
