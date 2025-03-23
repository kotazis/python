from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://www.saucedemo.com/'

driver.get(base_url)
driver.set_window_size(1920, 1080)

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
pass_input = driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")

button_login = driver.find_element(By.ID, "login-button").click()

button_backpack = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
button_bike_light = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
button_bolt_tshirt = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
button_fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
button_onesie = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]').click()
button_red_tshirt = driver.find_element(By.XPATH, '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()

button_cart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()

action = ActionChains(driver)
element = driver.find_element(By.ID, 'item_3_title_link')
action.move_to_element(element).perform()
