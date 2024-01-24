import pytest
from selenium.webdriver.common.by import By


class LoginPage1:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/v1/index.html"
        # self.login_icon = (By.XPATH, "//rz-user[contains(@class,'component')]")
        self.user_name_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.button_submit = (By.ID, "login-button")

    def open(self):
        self.driver.get(self.url)

    def login(self, user_name, password):
        self.driver.find_element(*self.user_name_field).send_keys(user_name)
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_button_submit(self):
        self.driver.find_element(*self.button_submit).click()
