from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/v1/index.html"
        # self.inventory_separate_items = (By.XPATH, "//div[@class='inventory_item']")
        self.inventory_items_list = (By.XPATH, "//div[@class='inventory_list']")
        sort_menu_selector = (By.XPATH, "// div[ @ id = 'inventory_filter_container'] / select")

    def open(self):
        self.driver.get(self.url)

    def get_number_of_products(self):
        products_element = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='inventory_item']")))

        product_elements = products_element.find_elements(By.XPATH, "//div[@class='inventory_item']")
        return len(product_elements)

    def click_product_sort_menu(self):
        sort_menu_element = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "// div[ @ id = 'inventory_filter_container'] / select")))
        sort_menu_element.click()

    def get_list_of_product_names(self):
        """ Get the name of all products on the PLP. """
        products = self.driver.find_elements(*self.inventory_items_list)
        return [item.text for item in products]

    def get_sort_products_a_to_z(self):
        sort_element = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//select[@class='product_sort_container']")))
        sort_element.click()







