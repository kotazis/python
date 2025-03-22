# Импортируем необходимые модули
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Аргумент для настроек запуска браузера, который не открывает само окно браузера
options.add_argument("--headless")

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://www.saucedemo.com/'

url = 'https://www.saucedemo.com/inventory.html'

driver.get(base_url)
driver.set_window_size(1920, 1080)

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys("standard_user")

pass_input = driver.find_element(By.XPATH, "//input[@id='password']")
pass_input.send_keys("secret_sauce")

button_login = driver.find_element(By.ID, "login-button")
button_login.click()

ger_url = driver.current_url

assert url == ger_url
print("Url верен")

text_product = driver.find_element(By.XPATH, "//span[@class='title']")
print(text_product.text)

assert text_product.text == "Products"
print('Заголовок корректен')
