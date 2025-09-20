from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By

firefox_service = FirefoxService(executable_path=r'D:\загрузки\geckodriver-v0.35.0-win64\geckodriver.exe')

driver = webdriver.Firefox(service=firefox_service)

driver.get("http://the-internet.herokuapp.com/login")

username_input = driver.find_element(By.ID, 'username')
username_input.send_keys('tomsmith')

password_input = driver.find_element(By.ID, 'password')
password_input.send_keys('SuperSecretPassword!')

login_button = driver.find_element(By.CLASS_NAME, 'radius')
login_button.click()

success_message = driver.find_element(By.CLASS_NAME, 'flash.success').text.strip()
print(success_message)

driver.quit()
