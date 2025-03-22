# Импортируем необходимые модули
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless")

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://www.saucedemo.com/'
url = 'https://www.saucedemo.com/inventory.html'

driver.get(base_url)
driver.set_window_size(1920, 1080)

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys("standard_use r")

pass_input = driver.find_element(By.XPATH, "//input[@id='password']")
pass_input.send_keys("secret_sauce")

button_login = driver.find_element(By.ID, "login-button")
button_login.click()

#ger_url = driver.current_url
#assert url == ger_url, "Url не верен"
#print("Url верен")

# поиск элемента с сообщением об ошибке авторизации
warning_element = driver.find_element(By.XPATH, "//h3[@data-test='error']")
# присваивание переменной текст сообщения ошибки
warning_text = warning_element.text

# проверка наличия ошибки
if warning_text == 'Epic sadface: Username is required' or warning_text == 'Epic sadface: Password is required' or warning_text == 'Epic sadface: Username and password do not match any user in this service':
    print("Ошибка авторизации")
else:
    print("Авторизация корректна")

# поиск кнопки закрытия сообщения об ошибке
error_button = driver.find_element(By.XPATH, "//button[@class='error-button']")
# нажатия на кнопку закрытия сообщения об ошибке
error_button.click()
print("click error button")

#text_product = driver.find_element(By.XPATH, "//span[@class='title']")
#print(text_product.text)
#assert text_product.text == "Products", "Заголовок не верен"
#print('Заголовок корректен')
