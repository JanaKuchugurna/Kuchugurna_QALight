from Kuchugurna_QALight.lecture_selenium.HW_9_rozetka.pages_rozetka.rozetka_page import ProductPage


class TestProductPage:
    def test_products_count_on_each_page(self, chrome):
        expected_product_count_on_page = 60
        # pages_to_check = 67  # Замініть на кількість сторінок, яку ви хочете перевірити

        product_page = ProductPage(driver=chrome)
        product_page.open()
        product_count = product_page.get_count_products_on_page()
        assert product_count == expected_product_count_on_page, "We don't have target products in per pages "

    def test_scroll_down_to_paginator(self, chrome):
        product_page = ProductPage(driver=chrome)
        product_page.open()
        product_page.scroll_to_paginator(product_page.paginator_1())
        assert product_page.paginator_1().is_enabled()
        # previous_but_pagination_disable = product_page.previous_but_pagination_disable()
        assert product_page.previous_button_in_pagination().is_displayed()
        assert product_page.next_button_in_pagination().is_enabled()

    def test_next_button_click_and_scroll_down(self, chrome):
        expected_product_count_on_page2 = 60
        product_page = ProductPage(driver=chrome)
        product_page.open()
        product_page.scroll_to_paginator(product_page.pagination_button2())
        product_page.pagination_button2().click()
        product_count = product_page.get_count_products_on_page()
        assert product_count == expected_product_count_on_page2
        assert 'page=2' in product_page.URL
