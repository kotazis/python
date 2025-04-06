from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

class Test():
    def test_select_product(self):
        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.set_window_size(1920,1080)

        user_name = WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="user-name"]')))
        user_name.send_keys("standard_user")

        password = WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
        password.send_keys("secret_sauce")

        button_login = WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "login-button")))
        button_login.click()

        button_sause_labs_backpack = WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')))
        button_sause_labs_backpack.click()

        button_cart = WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]')))
        button_cart.click()

        cart_page = WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="header_container"]/div[2]/span')))

        assert cart_page.text == "Your Cart", "Открыта не та страница"
        print("Страница верна")

start_test = Test()
start_test.test_select_product()
