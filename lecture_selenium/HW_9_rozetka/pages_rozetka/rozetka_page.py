from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class ProductPage:
    URL = 'https://rozetka.com.ua/notebooks/c80004/'

    first_locator = '//li[@class="pagination__item"]/a[contains(@class,"pagination__link pagination__link--active")]'
    # '//div[@class="pagination ng-star-inserted"]/a[contains(@class,"button button--gray")]'
    next_pag_locator = '//div[@class="pagination ng-star-inserted"]/a[contains(@title,"До наступної сторінки")]'
    previous_pag_locator = '//div[@class="pagination ng-star-inserted"]/a[contains(@title,"До попередньої сторінки")]'
    second_button_pag_locator = '//div[@class="pagination ng-star-inserted"]//a[contains(text(),"2")]'

    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def open(self):
        self.__driver.get(self.URL)

    def first_pagination(self):
        return self.__driver.find_element(By.XPATH, self.first_locator)

    def second_button_pagination(self):
        return self.__driver.find_element(By.XPATH, self.second_button_pag_locator)

    def next_pagination(self):
        return self.__driver.find_element(By.XPATH, self.next_pag_locator)

    def previous_pagination(self):
        return self.__driver.find_element(By.XPATH, self.previous_pag_locator)

    def count_products_on_page(self):
        locator = '//img[contains(@class,"lazy_img")]'
        products = self.__driver.find_elements(By.XPATH, locator)

        elements_to_check = 0
        for products in range(0, elements_to_check + 1):
            return elements_to_check

    def scroll_to_paginator(self):
        pass

    def previous_pagination_disable(self):
        # prev_button_enabled = WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located(By.XPATH, self.previous_pagination)
        # return disable in previous_pagination_disable.get attribute("class")
        prev_enable_button = self.previous_pagination().get_attribute("class")
        if 'disabled' in prev_enable_button:
            return True, "Кнопка 'назад' вимкнена."
        else:
            return False, "Кнопка 'назад' не вимкнена або не знайдена."
