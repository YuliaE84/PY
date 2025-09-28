import time
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import *

@pytest.fixture(scope="module")
def browser():
    service = Service(executable_path=r'D:\загрузки\geckodriver-v0.35.0-win64\geckodriver.exe')
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()


def test_shopping(browser):
    base_url = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    login_page = LoginPage(browser)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()

    inventory_page = InventoryPage(browser)
    for product_name in ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]:
        inventory_page.add_product_to_cart(product_name)

    inventory_page.go_to_cart()

    cart_page = CartPage(browser)
    cart_page.checkout()

    check_out_step_one_page = CheckOutStepOnePage(browser)
    check_out_step_one_page.fill_first_name("Yulia")
    check_out_step_one_page.fill_last_name("Egunova")
    check_out_step_one_page.fill_postal_code("454084")
    check_out_step_one_page.continue_checkout()

    overview_page = OverviewPage(browser)
    total_price = overview_page.get_total_amount()

    assert total_price == 58.29, f'Итоговая сумма отличается от ожидаемой ($58.29)'
