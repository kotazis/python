from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.lambdatest.com/selenium-playground/upload-file-demo'
driver.get(base_url)
driver.set_window_size(1920, 1080)

path = "D:\\PyCharm Community Edition 2024.3.3\\icon.png"

button = driver.find_element(By.XPATH, '//input[@id="file"]')

button.send_keys(path)

uploaded_file_path = button.get_attribute("value")
uploaded_file_name = uploaded_file_path.split("\\")[-1]

assert uploaded_file_name == "icon.png", "Названия не совпадают"
print("Названия совпадают")






