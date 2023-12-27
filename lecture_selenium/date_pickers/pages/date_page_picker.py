import self
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


# from selenium.webdriver.support.ui import Select


class PageDatePicker:
    URL = 'https://demoqa.com/date-picker'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.select_date_input = (By.ID, 'datePickerMonthYearInput')

    def open(self):
        self.driver.get(self.URL)

    def set_date_directly(self, selected_date):
        date_input = self.open_date_picker()
        date_input.send_keys(Keys.CONTROL + 'A')
        date_input.send_keys(Keys.DELETE)
        date_input.send_keys(selected_date)
        date_input.send_keys(Keys.ENTER)
        pass

    def open_date_picker(self) -> WebElement:
        element = self.driver.find_element(*self.select_date_input)
        element.click()
        return element

    def set_date_by_picker(self, selected_date) -> None:

        """

        :param selected_date: expected format --12/18/2023 where 12 is month, 18 is day, 2023 is year
        like string '12/18/2023'
        """
        month = selected_date.split('/')[0]
        try:
            month = int(month)
        except ValueError:
            month = month
        day = selected_date.split('/')[1]
        year = selected_date.split('/')[2]
        self.__set_date_by_picker(month=month, day=day, year=year)

    month = 12
    day = 2
    year = 2023

    def __set_date_by_picker(self, month: int | str, day: int, year: int) -> None:
        self.open_date_picker()
        self.__set_month(month=month)
        # self.__set_day(day=day)
        # self.__set_year(year=year)

    def __set_day_by_picker_with_scrolling(self, month: int | str, day: int, year: int):
        pass

    def scroll_to_target_year(self, target_year: int):
        locator_button_prev = (By.XPATH, '//button[contains(@class, "previous")]')
        locator_button_next = (By.XPATH, '//button[contains(@class, "next")]')
        prev_button = self.driver.find_element(*locator_button_prev)
        next_button = self.driver.find_element(*locator_button_next)

        if target_year > self.get_current_year():
            while target_year > self.get_current_year():
                next_button.click()
        elif target_year < self.get_current_year():
            while target_year < self.get_current_year():
                prev_button.click()

    def scroll_to_target_month(self, target_month: int):
        locator_button_prev = (By.XPATH, '//button[contains(@class, "previous")]')
        locator_button_next = (By.XPATH, '//button[contains(@class, "next")]')
        prev_button = self.driver.find_element(*locator_button_prev)
        next_button = self.driver.find_element(*locator_button_next)

        if target_month > self.get_current_month():
            next_button.click()
        else:
            prev_button.click()
        pass

    def get_current_year(self) -> int:
        current_year_in_picker_locator = (By.XPATH,
                                          '//div[@class="react-datepicker__header"]/div[contains(@class, "current")]')
        current_year = int(self.driver.find_element(*current_year_in_picker_locator).text.split(' ')[1])
        return current_year

    def get_current_month(self) -> int:
        current_month_in_picker_locator = (By.XPATH,
                                           '//div[@class="react-datepicker__header"]/div[contains(@class, "current")]')
        current_month = int(self.driver.find_element(*current_month_in_picker_locator).text.split(' ')[0])
        return current_month

    def get_current_day(self) -> int:
        # date = 'Choose Tuesday, December 26th, 2023'
        locator = '//div[contains(@class, "day--today")]'
        element = self.driver.find_element(By.XPATH, locator)
        date = element.get_attribute('aria-label')
        current_day = int(date.split(',')[1].strip().split(' ')[1].replace('th', ''))
        return current_day
        pass

    def __set_month(self, month: int | str):
        locator = '//select[contains(@class, "month-select")]'
        element = self.driver.find_element(By.XPATH, locator)
        select = Select(element)
        if type(month) is int:
            select.select_by_index(month)
            # select.select_by_value(month)
        elif type(month) is str:
            select.select_by_visible_text(month)
        else:
            raise TypeError(f'Month should have type of int or str, but given {type(month)}')

    def __set_day(self, day: int):

        pass

    def __set_year(self, year: int):
        locator = '//select[contains(@class,"year-select")]'
        element = self.driver.find_element(By.XPATH, locator)
        select = Select(element)
        select.select_by_value(year)

    def get_date(self):
        date_input = self.driver.find_element(*self.select_date_input)
        return date_input.get_attribute('value')
