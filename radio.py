from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.set_window_size(1920, 1080)

radio_button = driver.find_element(By.XPATH, '(//label[@class="custom-control-label"])[2]')
radio_button.click()

radio_input = driver.find_element(By.XPATH, '//*[@id="impressiveRadio"]')

if radio_input.is_selected():
    print("Radio button is active")
else:
    print("Radio button is NOT active")
