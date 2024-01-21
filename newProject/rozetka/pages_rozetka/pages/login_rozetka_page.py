from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://rozetka.com.ua/ua/"
        self.login_icon = (By.XPATH, "//rz-user[contains(@class,'component')]")
        self.email_field = (By.ID, "auth_email")
        self.password_field = (By.ID, "auth_pass")
        self.button_submit = (By.XPATH, "//button[contains(@class, 'button--large button--green')]")
        self.logged_in_username = (By.XPATH, "//span[@class='main-auth__user-name']")
        # self.input_button_to_cabinet = (By.XPATH, "//li [contains(@class, 'item--user')]")

    def open(self):
        self.driver.get(self.url)

    def click_login_icon(self):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(self.login_icon))
        self.driver.find_element(*self.login_icon).click()

    def login(self, email, password):
        self.driver.find_element(*self.email_field).send_keys(email)
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_button_submit(self):
        self.driver.find_element(*self.button_submit).click()

    def get_logged_in_username(self):
        return self.driver.find_element(*self.logged_in_username).text


