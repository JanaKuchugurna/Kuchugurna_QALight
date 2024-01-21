from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from Kuchugurna_QALight.lecture_selenium.HW_9_rozetka.locators import locators


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

    def paginator_1(self):
        element = self.__driver.find_element(By.XPATH, self.first_locator)
        return element

    def pagination_button2(self):
        return self.__driver.find_element(By.XPATH, self.second_button_pag_locator)

    def next_button_in_pagination(self):
        element = self.__driver.find_element(By.XPATH, self.next_pag_locator)
        return element

    def previous_button_in_pagination(self):
        element = self.__driver.find_element(By.XPATH, self.previous_pag_locator)
        return element

    def get_count_products_on_page(self) -> int:
        locator = '//img[contains(@class,"lazy_img")]'
        products = self.__driver.find_elements(By.XPATH, locator)

        return len(products)

    def scroll_to_paginator(self, first_pagination):
        actions = ActionChains(self.__driver)
        actions.move_to_element(first_pagination).perform()

    def previous_but_pagination_disable(self):
        # prev_btn_enable = self.__driver.find_element(By.XPATH, self.previous_pag_locator)
        # return not prev_btn_enable.is_enabled()
        prev_btn_enable = self.previous_button_in_pagination()
        return not prev_btn_enable.is_enabled()
        # prev_btn_enabled = self.previous_pagination().get_attribute('class')
        # if 'disabled' in prev_btn_enabled:
        #     return True
        # else:
        #     return False

    def next_but_pagination_enabled(self):
        next_button_enabled = self.next_button_in_pagination().is_enabled()
        return next_button_enabled
