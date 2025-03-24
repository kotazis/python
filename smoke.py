from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://www.saucedemo.com/'

driver.get(base_url)
driver.set_window_size(1920, 1080)

driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")

driver.find_element(By.ID, "login-button").click()

driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()

driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
driver.find_element(By.XPATH, '//*[@id="checkout"]').click()

driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Иван")
driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("Иванов")
driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("12345")

driver.find_element(By.XPATH, '//*[@id="continue"]').click()

backpack_price = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
backpack_price = float(backpack_price.text.replace("$", ""))

bikelight_price = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
bikelight_price = float(bikelight_price.text.replace("$", ""))

true_price = backpack_price + bikelight_price

item_total = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
item_total = float(item_total.text.replace("Item total: $", ""))

assert true_price == item_total, "Суммы не совпадают"
print("Суммы совпадают")

driver.find_element(By.XPATH, '//*[@id="finish"]').click()

checkout = driver.find_element(By.XPATH, '//*[contains(text(), "Thank you for your order!")]')
expected_value = 'Thank you for your order!'
assert checkout.text == expected_value, "Ошибка заказа"
print("Заказ успешно оформлен")

