import pytest
from selenium.webdriver.remote import webdriver
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def product_page_open(driver):
    driver.get("https://rozetka.com.ua/notebooks/c80004/")
    yield driver
