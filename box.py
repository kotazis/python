from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://demoqa.com/checkbox'
driver.get(base_url)
driver.set_window_size(1920, 1080)

check_box = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/label/span[1]')
check_box.click()

input_tree = driver.find_element(By.XPATH, '//*[@id="tree-node-home"]')

if input_tree.is_selected():
    print('Чек-бокс выбран')
else:
    print('Чек-бокс не выбран')

