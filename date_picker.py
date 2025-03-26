from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.set_window_size(1920, 1080)

date_input = driver.find_element(By.XPATH,'//input[@id="datePickerMonthYearInput"]')
date_input.send_keys(Keys.CONTROL + "a")
date_input.send_keys(Keys.DELETE)

ten_days = (datetime.now() + timedelta(days=10)).strftime("%m/%d/%Y")

date_input.send_keys(ten_days)
date_input.send_keys(Keys.RETURN)



