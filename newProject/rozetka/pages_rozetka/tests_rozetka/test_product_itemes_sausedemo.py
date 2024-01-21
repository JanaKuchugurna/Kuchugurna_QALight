from Rozetka.pages_rozetka.pages.product_itemes_page_sausedemo import ProductPage
from Rozetka.pages_rozetka.pages.login_sausedemo_page import LoginPage1


def test_count_products_on_page(driver):
    login_page = LoginPage1(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    login_page.click_button_submit()
    product_page = ProductPage(driver)
    product_page.click_product_sort_menu()
    product_page.get_sort_products_a_to_z()
    product_names = product_page.get_list_of_product_names()
    for i in range(len(product_names) - 1):
        assert product_names[i] <= product_names[i + 1], "Products {0} and {1} are not ordered correctly.".format(
            product_names[i], product_names[i + 1])
    print("test_sort_a_to_z finished successfully.")
