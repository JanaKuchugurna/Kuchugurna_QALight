from selenium.webdriver.common.by import By

#EXPAND_BUTTON = '//label[.="Home"]//ancestor::span[@class="rct-text"]/button'#захардкоджений документ
EXPAND_COLLAPSE_BUTTON = '//span[text()="{}"]//ancestor::span/button/*[contains(@class, "icon-expand")]' #розхардкоджений
# variable = 'HELLO'
# print(EXPAND_BUTTON.format(variable))
OUTPUT_RESULT = (By.XPATH, "//span[@class='text-success']")
CHECKED_ITEMS = (By.XPATH, 'svg[class="rct-icon rct-icon-check"]')