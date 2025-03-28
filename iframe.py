from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.lambdatest.com/selenium-playground/iframe-demo/'
driver.get(base_url)
driver.set_window_size(1920, 1080)

message = "Test message!!"
iframe = driver.find_element(By.XPATH, '//iframe[@id="iFrame1"]')
driver.switch_to.frame(iframe)

input_field = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]')
input_field.click()
input_field.send_keys(Keys.CONTROL + 'a')
input_field.send_keys(message)
input_field.send_keys(Keys.CONTROL + 'a')

driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/button[1]').click() #bold button
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/button[2]').click() #italic button
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/button[3]').click() #align center
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/button[4]').click() #strike through
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/button[5]').click() #underline

assert message == input_field.text, "Текс изменился!!"
print("Текст не изменился")





