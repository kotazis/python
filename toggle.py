import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
driver.get(base_url)
driver.set_window_size(1920, 1080)

actions = ActionChains(driver)

value = driver.find_element(By.XPATH, '//*[@id="f"]')
first_value = value.text

slider = driver.find_element(By.XPATH, '//input[@class="slider-square"]')
actions.click_and_hold(slider).move_by_offset(-100, 0).release().perform()

second_value = value.text

if first_value == second_value:
    print("Ошибка, значения не изменились ")
else:
    print("Значения изменились")



