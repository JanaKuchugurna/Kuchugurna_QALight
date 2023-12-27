from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Kuchugurna_QALight.HW8_check_boxes.locators.checkbox_locators import EXPAND_COLLAPSE_BUTTON


class PageCheckboxes:
    URL = 'https://demoqa.com/checkbox'

    def __init__(self, driver: WebDriver):
        self.__check_uncheck_label = None
        self.driver: WebDriver = driver
        self.expand_button_locator = EXPAND_COLLAPSE_BUTTON

    def open(self):
        print(f'opening page: {self.URL}')
        self.driver.get(self.URL)
        return self

    def __expand_or_collapse_folder(self, name,
                                    expand=True):  # приватний метод з двома підкресленнями щоб не показувалось в тестах
        if expand:
            state = 'close'
        else:
            state = 'open'
        element = self.driver.find_element(By.XPATH, self.expand_button_locator.format(name))
        if f'expand-{state}' in element.get_attribute('class'):
            element.click()

    def expand_folder(self, name):
        self.__expand_or_collapse_folder(name, expand=True)

    def collapse_folder(self, name):
        self.__expand_or_collapse_folder(name, expand=False)

    def check_folders(self, *names):
        self.__check_or_uncheck_folders(*names, check=True)

    def uncheck_folders(self, *names):
        self.__check_or_uncheck_folders(*names, check=False)

    def __check_or_uncheck_folders(self, *names: str, check=True):
        for name in names:
            check_uncheck_input = f'{self.__check_uncheck_label.format(name.lower())}/input'
            check_uncheck_label = f'{check_uncheck_input}/..'
            _input = self.__driver.find_element(By.XPATH, check_uncheck_input)
            _label = self.__driver.find_element(By.XPATH, check_uncheck_label)
            if check:
                if not _input.is_selected():
                    _label.cklick()
                else:
                    if _input.is_selected():
                        _label.cklick()
    #def get_output_result(self):
