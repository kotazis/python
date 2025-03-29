import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://the-internet.herokuapp.com/javascript_alerts'
driver.get(base_url)
driver.set_window_size(1920, 1080)

driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button').click()
time.sleep(2)
driver.switch_to.alert.accept()

driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button').click()
time.sleep(2)
driver.switch_to.alert.dismiss()

driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button').click()
time.sleep(2)
driver.switch_to.alert.send_keys("123qwe")
time.sleep(2)
driver.switch_to.alert.accept()





