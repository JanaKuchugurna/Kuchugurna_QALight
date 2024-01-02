from Kuchugurna_QALight.lecture_selenium.HW_9_rozetka.pages_rozetka.rozetka_page import ProductPage


class TestProductPage:
    def test_products_count_on_each_page(self, chrome):
        target_products_per_page = 60
        # pages_to_check = 67  # Замініть на кількість сторінок, яку ви хочете перевірити

        product_page = ProductPage(driver=chrome)
        product_page.open()
        elements_to_check = product_page.count_products_on_page()
        assert elements_to_check == target_products_per_page, "We don't have target products in per pages "

    def test_previous_pagination_disable(self,):
        product_page = ProductPage()
        product_page.open()
        product_page.scroll_to_paginator()

