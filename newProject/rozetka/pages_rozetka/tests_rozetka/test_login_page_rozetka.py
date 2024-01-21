from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Rozetka.pages_rozetka.pages.login_rozetka_page import LoginPage


def test_login_field(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.click_login_icon()
    login_page.login("iaroslav.kuchugurnyi@gmail.com", "12L0000l")
    login_page.click_button_submit()
    logged_in_username = login_page.get_logged_in_username()
    expected_username = "Ярослав Кучугурний"
    assert logged_in_username == expected_username

