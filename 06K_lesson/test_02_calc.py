import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.usefixtures("browser")
def test_calculator(browser): 
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    try:
        delay_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#delay'))
        )
        delay_input.clear()
        delay_input.send_keys('45')

        seven_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='7']"))
        )
        seven_button.click()

        plus_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='+']"))
        )
        plus_button.click()

        eight_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='8']"))
        )
        eight_button.click()

        equals_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='=']"))
        )
        equals_button.click()

        result_field = WebDriverWait(browser, 50).until(
            EC.text_to_be_present_in_element((By.ID, 'result'), '15')
        )
    
    finally:
         pass
