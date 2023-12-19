from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def select_radio_button(driver: WebDriver, name: str):
    locator = f'//label[text()="{name}"]//ancestor::div[contains(@class, "radio")]'
    # locator = f'//label[text()="Yes"]//ancestor::div[contains(@class, "radio")]'
    locator_selected_text = '//p[@class="mt-3"]'
    locator_selected_name = f'//span[@class"text-success" and text() = "{name}"]'
    input_ = f'{locator}/input'
    label_ = f'{locator}/label'

    element_input = driver.find_element(By.XPATH, input_)
    element_label = driver.find_element(By.XPATH, label_)
    if not element_input.is_enabled():
        driver.execute_script('arguments[0].removeAttribute("disabled");', element_input)
        element_label.click()
        assert element_input.is_selected(), "'No' radio button is not selected"
    else:
        if not element_input.is_selected():
            element_label.click()

    locator_selected_text = driver.find_element(By.XPATH, locator_selected_text)
    locator_selected_name = driver.find_element(By.XPATH, locator_selected_name)

    assert locator_selected_text.is_displayed(), "'You have selected' text is not displayed"
    assert locator_selected_name.text == name, f"Selected radio button is incorrect {name}"


def dictionary_of_radio_but(driver: WebDriver):
    d = {}
    locator = '//div[contains(@class, "radio")]'  # finding all 3 radiobuttons
    list_of_radio = driver.find_elements(By.XPATH, locator)
    assert list_of_radio, "Elements are not found"
    for div in list_of_radio:
        radio_but_name = div.text
        radio_button_locator = f'//label[text()="{radio_but_name}"]//ancestor::div[contains(@class, "radio")]/input'
        radio_but = driver.find_element(By.XPATH, radio_button_locator)
        radio_button_enabled = radio_but.is_enabled()
        radio_button_selected = radio_but.is_selected()
        dict[radio_but_name] = {'enabled': radio_button_enabled, 'selected': radio_button_selected}

    print(d)
