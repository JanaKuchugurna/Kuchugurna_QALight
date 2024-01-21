
from selenium.webdriver import Chrome
from selenium.webdriver.remote import webdriver
import pytest


@pytest.fixture(scope='session')
def chrome():
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument("--headless")
    chrome_option.add_argument("--use_subprocess")
    driver = webdriver.Chrome(options=chrome_option)
    yield driver
    driver.quit()


# @pytest.fixture(scope='session')
# def chrome():
#     driver = Chrome()
#     yield driver
#     driver.quit()

# @pytest.fixture()
# def get_chrome_driver(chrome):
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(6)
#     yield
#     driver.quit()
#
#
# @pytest.fixture()
# def login_fields(chrome):
#     chrome.get('https://rozetka.com.ua/ua/')
#     yield chrome
