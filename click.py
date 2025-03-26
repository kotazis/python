from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://demoqa.com/buttons'
driver.get(base_url)
driver.set_window_size(1920, 1080)

action = ActionChains(driver)

doubleclick_button = driver.find_element(By.XPATH, '//*[@id="doubleClickBtn"]')
action.double_click(doubleclick_button).perform()

rightclick_button = driver.find_element(By.XPATH, '//*[@id="rightClickBtn"]')
action.context_click(rightclick_button).perform()

