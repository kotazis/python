from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Test():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        base_url = 'https://www.saucedemo.com/'
        self.driver.get(base_url)
        self.driver.set_window_size(1920,1080)


    def log_in(self):
        user_name = WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="user-name"]')))
        user_name.send_keys("standard_user")

        password = WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
        password.send_keys("secret_sauce")

        button_login = WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.ID, "login-button")))
        button_login.click()


    def add_item(self):
        button_sause_labs_backpack = WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')))
        button_sause_labs_backpack.click()

        button_cart = WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]')))
        button_cart.click()

    
    def check_page(self):
        cart_page = WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="header_container"]/div[2]/span')))
        assert cart_page.text == "Your Cart", "Открыта не та страница"
        print("Страница верна")


start_test = Test()
start_test.log_in()
start_test.add_item()
start_test.check_page()
