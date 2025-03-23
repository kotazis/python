import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://www.saucedemo.com/'

driver.get(base_url)
driver.set_window_size(1920, 1080)

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys("standard_user")

pass_input = driver.find_element(By.XPATH, "//input[@id='password']")
pass_input.send_keys("secret_sauce")

button_login = driver.find_element(By.ID, "login-button")
button_login.click()


now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
name_scr = 'screenshot.png' + now_date + '.png'

driver.save_screenshot("D:\\PyCharm Community Edition 2024.3.3\\proj1\\screen\\" + name_scr)
