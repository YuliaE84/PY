import time
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def browser():
    service = Service(executable_path=r"D:\загрузки\geckodriver-v0.35.0-win64\geckodriver.exe")
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()
    
def test_shopping(browser):
    base_url = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    browser.get(base_url)
    user_input = browser.find_element(By.ID, "user-name")
    user_input.send_keys(username)
    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys(password)
    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()

    products = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    for product_name in products:
        add_to_cart_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item_description']//button"))
        )
        add_to_cart_btn.click()

    cart_icon = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()

    checkout_button = browser.find_element(By.ID, "checkout")
    checkout_button.click()

    first_name_input = browser.find_element(By.ID, "first-name")
    first_name_input.send_keys("Yulia")
    last_name_input = browser.find_element(By.ID, "last-name")
    last_name_input.send_keys("Egunova")
    postal_code_input = browser.find_element(By.ID, "postal-code")
    postal_code_input.send_keys("454084")
    continue_button = browser.find_element(By.ID, "continue")
    continue_button.click()

    total_amount = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    ).text
    total_price = float(total_amount.replace("Total: $", ""))

    assert total_price == 58.29, f"Итоговая сумма отличается от ожидаемой ($58.29)"
