from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")

sleep(5)

blue_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
blue_button.click()

sleep(5)
