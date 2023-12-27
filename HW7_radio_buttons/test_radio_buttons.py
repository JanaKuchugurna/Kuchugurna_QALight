import pytest
from selenium.webdriver import Chrome
from Kuchugurna_QALight.HW7_radio_buttons.locators_radio_buttons import select_radio_button, dictionary_of_radio_but


@pytest.fixture(scope='class')
def chrome(request):
    driver = Chrome()
    if request.cls:
        request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.mark.usefixtures('chrome')
class TestRadioButtons:

    def test_select_button_yes(self):
        self.driver.get('https://demoqa.com/radio-button')
        select_radio_button(driver=self.driver, name='Yes')


    def test_select_button_impressive(self):
        self.driver.get('https://demoqa.com/radio-button')
        select_radio_button(driver=self.driver, name='Impressive')


    def test_select_button_no(self):
        self.driver.get('https://demoqa.com/radio-button')
        select_radio_button(driver=self.driver, name='No')


    def test_dictionary_of_radio_but(self):
        self.driver.get('https://demoqa.com/radio-button')
        dictionary_of_radio_but(self.driver)
