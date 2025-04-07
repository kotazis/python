from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Login:
    def __init__(self, url):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        self.driver.get(url)
        self.driver.set_window_size(1920, 1080)


    def authorization(self, login_name, password):
        user_name = WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="user-name"]')))
        user_name.send_keys(login_name)

        password_input = WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
        password_input.send_keys(password)

        button_login = WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.ID, "login-button")))
        button_login.click()


    def get_driver(self):
        return self.driver
