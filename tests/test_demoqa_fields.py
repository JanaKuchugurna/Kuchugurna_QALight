import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def get_chrome_driver():
    driver = webdriver.Chrome()
    # driver.implicitly_wait(6)
    yield driver
    driver.quit()


@pytest.fixture()
def login_fields(get_chrome_driver):
    get_chrome_driver.get('https://demoqa.com/text-box')
    yield get_chrome_driver


def test_name_field(login_fields):
    login_user = "Jana"
    driver = login_fields
    full_name_field = driver.find_element(By.XPATH, '//input[@id="userName"]')
    time.sleep(6)
    full_name_field.send_keys(login_user)
    assert full_name_field.is_displayed()


def test_password_field(login_fields):
    email = "jana.kuchugurna@gmail.com"
    driver = login_fields
    email_field = driver.find_element(By.XPATH, '//input[@id="userEmail"]')
    email_field.send_keys(email)
    assert email_field.is_displayed()


def test_current_address(login_fields):
    cur_address = "Bulachovskoho 34 Kyiv"
    driver = login_fields
    current_address = driver.find_element(By.XPATH, '//textarea[@id = "currentAddress"]')
    current_address.send_keys(cur_address)
    assert current_address.is_displayed()


def test_permanent_address(login_fields):
    per_address = "Lehovecka 12 Prague 14"
    driver = login_fields
    permanent_address = driver.find_element(By.ID, "permanentAddress")
    permanent_address.send_keys(per_address)
    assert permanent_address.is_displayed()


def test_button_submit(login_fields):
    driver = login_fields
    button_submit = driver.find_element(By.XPATH, '//button[@id="submit"]')
    button_submit.click()
    assert button_submit.is_displayed()
