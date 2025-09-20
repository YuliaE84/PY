from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By

firefox_service = FirefoxService(executable_path=r'D:\загрузки\geckodriver-v0.35.0-win64\geckodriver.exe')

driver = webdriver.Firefox(service=firefox_service)

driver.get("http://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(By.TAG_NAME, 'input')
input_field.send_keys("Sky")

sleep(5)

input_field.clear()

sleep(5)

input_field.send_keys("Pro")

driver.quit()
