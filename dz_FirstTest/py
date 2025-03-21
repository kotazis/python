# Импортируем необходимые модули
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Создаём объект настроек для браузера
options = webdriver.ChromeOptions()

# Добавляем опцию, чтобы браузер не закрывался автоматически после завершения скрипта
options.add_experimental_option("detach", True)

# Инициализируем веб-драйвер Chrome с установленными настройками
# ChromeDriverManager автоматически скачивает и устанавливает подходящую версию драйвера
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# Задаём URL веб-сайта
base_url = 'https://www.saucedemo.com/'

# Открываем ссылку в браузере
driver.get(base_url)

# Устанавливаем размер окна
driver.set_window_size(1920, 1080)

# Присваиваем переменной элемент который находим с помощи функции find_element через XPATH
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
# Отправляем в переменную(элемент на странице) строку
user_name.send_keys("standard_user")

# Тоже-самое, меняется XPATH элементов страницы, а именно поля ввода логина и пороля
pass_input = driver.find_element(By.XPATH, "//input[@id='password']")
pass_input.send_keys("secret_sauce")

# Присваиваем переменной кнопку которую находим с помощи функции find_element через ID
button_login = driver.find_element(By.ID, "login-button")
# С помощи функции делаем клик на кнопку которая присвоена переменной
button_login.click()
# Переменная для текущего url
ger_url = driver.current_url
# Url который нам нужен
url = 'https://www.saucedemo.com/inventory.html'
# Сравнение текущего и нужного нам url
assert url == ger_url
print("Url верен")
# Поиск элемента на странице каталога
text_product = driver.find_element(By.XPATH, "//span[@class='title']")
print(text_product.text)
# Сравнение найденного значение из страницы каталога с нужной нам строкой
assert text_product.text == "Products"
print('Заголовок корректен')
