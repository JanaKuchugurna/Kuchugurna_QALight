from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# link = "https://rozetka.com.ua/ua/"
# driver = webdriver.Chrome()
# driver.get(link)


# search_string = driver.find_element(By.XPATH, "//input[@name='search']")
# search_string.send_keys("Зоотовари")
#
# button_search = driver.find_element(By.XPATH, "//button[contains(@class, 'search-form__submit')]")
# button_search.click()
# product_name_check = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[@class='portal__heading ng-star-inserted']"))).text
# product_name = "Зоотовари"
# assert product_name_check == product_name, f'Test do not passed {product_name_check}'


# def click_button_that_you_are_people(self):
#     self.driver.find_elements(*self.button_that_you_are_people).click()

# def search_for_product(self, product_name):
#     search_input = self.driver.find_elements(*self.search_input)
#     # search_input.clear()
#     search_input.send_keys(product_name)
#     search_button = self.driver.find_elements(*self.search_button)
#     search_button.click()
#
# def get_search_results(self):
#     return self.driver.find_elements(*self.results)
class ProductSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://rozetka.com.ua/search"
        # self.search_input = (By.XPATH, "//input[@name='search']")
        # self.search_button = (By.XPATH, "//button[contains(@class, 'search-form__submit')]")
        # self.results = (By.XPATH, "//h1[@class='portal__heading ng-star-inserted']")
        # self.button_that_you_are_people = "//input[@type='checkbox']"

    def open(self):
        self.driver.get(self.url)


    def search_product_and_click_ok(self, product_name):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='search']")))
        search_input.send_keys(product_name)

        search_button = self.driver.find_element(By.XPATH, "//button[contains(@class, 'search-form__submit')]")
        search_button.click()

        search_result = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[@class='portal__heading ng-star-inserted']")))
        return search_result.text
