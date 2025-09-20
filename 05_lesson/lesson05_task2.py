from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/dynamicid")

sleep(5)

blue_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
blue_button.click()

print("Кнопка успешно нажата!")

sleep(5)
