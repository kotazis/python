import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker


fake = Faker("ru_RU")

first_name = fake.first_name()
last_name = fake.last_name()
postal_code = fake.postcode()

items = {
    "1": ("Sauce Labs Backpack", '//*[@id="add-to-cart-sauce-labs-backpack"]'),
    "2": ("Sauce Labs Bike Light", '//*[@id="add-to-cart-sauce-labs-bike-light"]'),
    "3": ("Sauce Labs Bolt T-Shirt", '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'),
    "4": ("Sauce Labs Fleece Jacket", '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'),
    "5": ("Sauce Labs Onesie", '//*[@id="add-to-cart-sauce-labs-onesie"]'),
    "6": ("Test.allTheThings() T-Shirt (Red)", '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
}

print("Приветствую тебя в нашем интернет - магазине")
print("Выбери один из следующих товаров и укажи его номер:")

for key, value in items.items():
    print(f"{key} - {value[0]}")

item_number = input("Выберите номер: ")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://www.saucedemo.com/'

driver.get(base_url)
driver.set_window_size(1920, 1080)

driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")

driver.find_element(By.ID, "login-button").click()

if item_number in items:
    driver.find_element(By.XPATH, items[item_number][1]).click()
    print(f"Добавлен товар: {items[item_number][0]}")
else:
    print("Ошибка: такого товара нет.")

time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
driver.find_element(By.XPATH, '//*[@id="checkout"]').click()

driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys(fake.first_name())
driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys(fake.last_name())
driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys(fake.postcode())

time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="continue"]').click()

item_price = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
item_price = float(item_price.text.replace("$", ""))

item_total = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
item_total = float(item_total.text.replace("Item total: $", ""))

assert item_price == item_total, "Суммы не совпадают"
print("Суммы совпадают")

time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="finish"]').click()

checkout = driver.find_element(By.XPATH, '//*[contains(text(), "Thank you for your order!")]')
expected_value = 'Thank you for your order!'
assert checkout.text == expected_value, "Ошибка заказа"
print("Заказ успешно оформлен")
