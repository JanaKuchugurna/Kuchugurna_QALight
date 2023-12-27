from selenium.webdriver import Chrome

from Kuchugurna_QALight.lecture_selenium.date_pickers.pages.date_page_picker import PageDatePicker


class TestDatePicker:

    def test_select_date(self, chrome):
        target_date = '12/07/2025'
        page = PageDatePicker(driver=chrome)
        page.open()
        page.open_date_picker()
        # page.set_date_directly(target_date)
        # assert page.get_date() == target_date
        # date = 'February/18/2023'
        # page.set_date_by_picker('February/18/2023'), f'//div[contains(@aria-label, "{date.split("/")[0]}")][contains(@aria-label, "{date.split("/")[1]}")][contains(@aria-label, "{date.split("/")[2]}")]'
        # page.set_date_by_picker('0/18/2023')
        target_year = int(target_date.split('/')[-1])
        page.scroll_to_target_year(target_year)
        target_month = int(target_date.split('/')[1])
        page.scroll_to_target_month(target_month)
        # page.set_target_day()
        pass

    def test_current_day(self, chrome):
        page = PageDatePicker(chrome)
        page.open()
        page.open_date_picker()
        print(page.get_current_day())

    def test_scroll_to_target_date(self, chrome):
        target_date = '11/28/2020'
        page = PageDatePicker(chrome)
        page.open()
        page.open_date_picker()




