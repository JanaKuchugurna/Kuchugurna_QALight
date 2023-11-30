import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def get_chrome_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(6)
    yield driver
    driver.quit()


@pytest.fixture()
def goto_dyn_prop_page(get_chrome_driver):
    get_chrome_driver.get('https://demoqa.com/dynamic-properties')
    yield get_chrome_driver


def test_button_enables(goto_dyn_prop_page):
    driver = goto_dyn_prop_page
    target_button = driver.find_element(By.ID, 'enableAfter')
    assert target_button.is_displayed()
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable(target_button))
    assert target_button.is_enabled()


def test_button_text_color_changes(goto_dyn_prop_page):
    driver = goto_dyn_prop_page
    # button_text_color = driver.find_element(By.CSS_SELECTOR, 'button[id="colorChange"]')
    button_text_color = WebDriverWait(driver, 6).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, 'button[id="colorChange"]')))
    initial_color = button_text_color.value_of_css_property('color')
    current_color = button_text_color.value_of_css_property('color')
    assert initial_color != current_color, "Колір тексту на кнопці не був змінений"


def test_button_appears(goto_dyn_prop_page):
    driver = goto_dyn_prop_page
    target_button = WebDriverWait(driver, 6).until(ec.visibility_of_element_located((By.ID, 'visibleAfter')))
    assert target_button.is_displayed()
