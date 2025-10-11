import allure
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
    """
    Инициализация и закрытие браузера Firefox.
    """
    service = Service(executable_path=r'D:\загрузки\geckodriver-v0.35.0-win64\geckodriver.exe')
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()

@allure.feature("Покупка товаров на SauceDemo")
@allure.severity("blocker")
@allure.title("Оформление покупки с несколькими товарами")
@allure.description("Тестирует покупку товаров на сайте SauceDemo с последующим оформлением заказа.Включает проверку цены")

def test_shopping(browser):
    base_url = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    with allure.step("Открытие главной страницы"):
        browser.get(base_url)

    with allure.step("Авторизация пользователя"):    
        login_page = LoginPage(browser)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login_button()

    with allure.step("Выбор и добавление товаров в корзину"):
        inventory_page = InventoryPage(browser)
        for product_name in ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]:
            inventory_page.add_product_to_cart(product_name)

    with allure.step("Переход в корзину"):
        inventory_page.go_to_cart()

    with allure.step("Начало оформления заказа"):
        cart_page = CartPage(browser)
        cart_page.checkout()
    
    with allure.step("Введение личных данных"):
        check_out_step_one_page = CheckOutStepOnePage(browser)
        check_out_step_one_page.fill_first_name("Yulia")
        check_out_step_one_page.fill_last_name("Egunova")
        check_out_step_one_page.fill_postal_code("454084")
        check_out_step_one_page.continue_checkout()
    
    with allure.step("Получение итоговой суммы заказа"):
        overview_page = OverviewPage(browser)
        total_price = overview_page.get_total_amount()
