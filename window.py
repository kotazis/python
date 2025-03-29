import time

from faker import Faker

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/browser-windows'
driver.get(base_url)
driver.set_window_size(1920, 1080)

new_tab = driver.find_element(By.XPATH, '//button[@id="tabButton"]')
new_tab.click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])

new_window = driver.find_element(By.XPATH, '//*[@id="windowButton"]')
new_window.click()
driver.switch_to.window(driver.window_handles[2])
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])





