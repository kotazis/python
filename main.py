from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from LoginPage import Login


class Test:
    @staticmethod
    def add_item(product_number):
        products = {
            1: ("Sauce Labs Backpack", '//*[@id="add-to-cart-sauce-labs-backpack"]'),
            2: ("Sauce Labs Bike Light", '//*[@id="add-to-cart-sauce-labs-bike-light"]'),
            3: ("Sauce Labs Bolt T-Shirt", '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'),
            4: ("Sauce Labs Fleece Jacket", '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'),
            5: ("Sauce Labs Onesie", '//*[@id="add-to-cart-sauce-labs-onesie"]'),
            6: ("Test.allTheThings() T-Shirt (Red)", '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
        }

        product_name, path = products[product_number]

        button = WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, path)))
        button.click()
        print(f"{product_name} добавлен в корзину")

        button_cart = WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]')))
        button_cart.click()


    @staticmethod
    def check_page():
        cart_page = WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="header_container"]/div[2]/span')))
        assert cart_page.text == "Your Cart", "Открыта не та страница"
        print("Страница верна")

login = Login('https://www.saucedemo.com/')
login.authorization("standard_user", "secret_sauce")

driver = login.get_driver()
start_test = Test()
start_test.add_item(1)
start_test.check_page()
