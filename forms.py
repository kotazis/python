from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.lambdatest.com/selenium-playground/simple-form-demo'
driver.get(base_url)
driver.set_window_size(1920, 1080)

message = "Сообщение"
first_input = driver.find_element(By.XPATH, '//input[@id="user-message"]')
first_input.send_keys(message)

driver.find_element(By.XPATH, '//button[@id="showInput"]').click()

first_output = driver.find_element(By.XPATH, '//*[@id="message"]')

assert message == first_output.text, "Текст не совпадает"
print("Текст совпадает")

sum_first = driver.find_element(By.XPATH, '//*[@id="sum1"]')
sum_second = driver.find_element(By.XPATH, '//*[@id="sum2"]')

one = "1"
two = "2"
sum_first.send_keys(one)
sum_second.send_keys(two)

second_output = driver.find_element(By.XPATH, '//*[@id="addmessage"]')

driver.find_element(By.XPATH, '//*[@id="gettotal"]/button').click()

assert second_output.text == str(int(one) + int(two)), "Сумма не совпадает"
print("Сумма совпадает")






