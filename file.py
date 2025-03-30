import glob
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


path = "D:\\PyCharm Community Edition 2024.3.3\\proj1\\123"

options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : path}
options.add_experimental_option('prefs', prefs)
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.lambdatest.com/selenium-playground/download-file-demo'
driver.get(base_url)
driver.set_window_size(1920, 1080)

driver.find_element(By.XPATH, '//*[@id="__next"]/div/section[2]/div/div/div/div/a/button').click()
time.sleep(2)

file_name = "123.pdf"
file_path = path + file_name
assert os.access(file_path, os.F_OK) == True
print("Файл в директории")

files = glob.glob(os.path.join(path, '*.*'))
for file in files:
    a = os.path.getsize(file)
    if a > 10:
        print("Файл не пуст")
    else:
        print("Файл пуст")










