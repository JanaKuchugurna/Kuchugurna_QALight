import pytest

from newProject.uiTesting.pages_rozetka.pages.search_field_page import ProductSearchPage


@pytest.mark.smoke()
def test_product_search(driver):
    search_page = ProductSearchPage(driver)
    search_page.open()
    product_name = "Зоотовари"
    result_text = search_page.search_product_and_click_ok(product_name)
    assert product_name in result_text
