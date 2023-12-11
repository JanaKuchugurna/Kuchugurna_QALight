# from urllib import request
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome


@pytest.fixture()
def driver():
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def fixture_1():
    print('This is executed before test')
    yield
    print('\nThis is executed after test')


@pytest.fixture(scope='class')
def chrome(request):
    driver = Chrome()
    if request.cls:
        request.cls.driver = driver
    yield driver
    driver.quit()
