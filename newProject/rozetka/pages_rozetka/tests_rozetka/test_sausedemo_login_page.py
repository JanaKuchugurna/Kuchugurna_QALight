from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Rozetka.pages_rozetka.pages.login_sausedemo_page import LoginPage1
from Rozetka.pages_rozetka.pages.product_itemes_page_sausedemo import ProductPage


def test_count_products_on_page(driver):
    login_page = LoginPage1(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    login_page.click_button_submit()
    product_page = ProductPage(driver)
    number_of_products = product_page.get_number_of_products()
    print(f"Кількість продуктів на сторінці: {number_of_products}")
    expected_number_of_products = 6
    assert number_of_products == expected_number_of_products




