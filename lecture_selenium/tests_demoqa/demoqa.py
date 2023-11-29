from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://demoqa.com/text-box')

full_name_field = driver.find_element(By.XPATH, '//input[@id="userName"]')
search_input_text = "Jana"
full_name_field.send_keys(search_input_text)

email_field = driver.find_element(By.XPATH, '//input[@id="userEmail"]')
search_input_text = "jana.kuchugurna@gmail.com"
email_field.send_keys(search_input_text)

current_address = driver.find_element(By.XPATH, '//textarea[@id = "currentAddress"]')
search_input_text = "Bulachovskoho 34 Kyiv"
current_address.send_keys(search_input_text)

permanent_address = driver.find_element(By.ID, "permanentAddress")
search_input_text = "Lehovecka 12 Prague 14"
permanent_address.send_keys(search_input_text)




