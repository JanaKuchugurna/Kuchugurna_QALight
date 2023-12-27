from Kuchugurna_QALight.HW8_check_boxes.pages.page_checkboxes import PageCheckboxes
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver


class TestCheckbox:

    def test_1(self, driver):
        directories = ['Home', 'Documents', 'Office']
        targets_for_check = ['Public', 'Private']
        #targets_for_uncheck = ['Veu']
        driver: WebDriver = Chrome()
        page = PageCheckboxes(driver)
        page.open()
        page.expand_folder(directories)
        page.check_folders(*targets_for_check)
        #page.uncheck_folders(*targets_for_uncheck)
        pass
