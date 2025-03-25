import time

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

driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")

driver.find_element(By.ID, "login-button").click()

driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()

driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()

time.sleep(1)

driver.back()

time.sleep(1)

driver.forward()


