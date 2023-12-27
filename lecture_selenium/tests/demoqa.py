from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://demoqa.com/text-box')

input_name = "Jana"
input_email = "jana.kuchugurna@gmail.com"
input_current_address = "Bulachovskoho 34 Kyiv"
input_permanent_address = "Lehovecka 12 Prague 14"

full_name_field = driver.find_element(By.XPATH, '//input[@id="userName"]')
full_name_field.send_keys(input_name)

email_field = driver.find_element(By.XPATH, '//input[@id="userEmail"]')
email_field.send_keys(input_email)

current_address = driver.find_element(By.XPATH, '//textarea[@id = "currentAddress"]')
current_address.send_keys(input_current_address)

permanent_address = driver.find_element(By.ID, "permanentAddress")
permanent_address.send_keys(input_permanent_address)
