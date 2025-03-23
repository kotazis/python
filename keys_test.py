from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://www.saucedemo.com/'

driver.get(base_url)
driver.set_window_size(1920, 1080)

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
pass_input = driver.find_element(By.XPATH, "//input[@id='password']")

user_name.send_keys(Keys.CONTROL + 'a')
user_name.send_keys(Keys.DELETE)
pass_input.send_keys(Keys.CONTROL + 'a')
pass_input.send_keys(Keys.DELETE)

user_name.send_keys("standard_user")
pass_input.send_keys("secret_sauce")

button_login = driver.find_element(By.ID, "login-button").click()
