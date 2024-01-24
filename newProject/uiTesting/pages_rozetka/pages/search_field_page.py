from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ProductSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://rozetka.com.ua/search"
        self.search_input = (By.XPATH, "//input[@name='search']")
        self.search_button = (By.XPATH, "//button[contains(@class, 'search-form__submit')]")
        self.results = (By.XPATH, "//h1[@class='portal__heading ng-star-inserted']")
        # self.button_that_you_are_people = "//input[@type='checkbox']"

    def open(self):
        self.driver.get(self.url)

    def search_product_and_click_ok(self, product_name):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(*self.search_input))
        search_input.send_keys(product_name)

        search_button = self.driver.find_element(*self.search_button)
        search_button.click()

        search_result = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(*self.results))
        return search_result.text
