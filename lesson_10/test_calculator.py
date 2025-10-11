"""
Автоматизированный тест калькулятора на сайте bonigarcia.dev.
Тест включает: запуск браузера, переход на страницу калькулятора,
установку задержки, ввод выражения (7 + 8), получение результата и завершение работы.
"""
import allure
import pytest
from selenium import webdriver
from calculator_page import SlowCalculatorPage


@pytest.fixture(scope="function")
def browser():
    """
    Фикстура, создающая экземпляр веб-драйвера и завершающая сессию после завершения теста.
    :scope function: Область видимости — один сеанс на каждую отдельную функцию.
    """
    with allure.step("Запуск браузера"):
        driver = webdriver.Chrome()
        yield driver
        with allure.step("Закрытие браузера"):
            driver.quit()

@allure.id("Calc-1")
@allure.story("Проверка работы калькулятора")
@allure.title("Проверка работы онлайн-калькулятора")
@allure.description("Проверка отображения верного результата")
@allure.severity("blocker")
def test_calculator(browser):
    """
    Основной тестовый сценарий для проверки работы онлайн-калькулятора.
    Осуществляются действия: установка задержки, расчет суммы (7 + 8),
    ожидание результата и проверка его правильности.
    """
    with allure.step("Переход на страницу калькулятора"):
        browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        browser.calculator_page = SlowCalculatorPage(browser)

    with allure.step("Установка задержки на расчеты"):
        browser.calculator_page.set_delay('45')

    with allure.step("Последовательности команд: 7 + 8 ="):
        browser.calculator_page.click_button(SlowCalculatorPage.BUTTON_7_LOCATOR)
        browser.calculator_page.click_button(SlowCalculatorPage.PLUS_BUTTON_LOCATOR)
        browser.calculator_page.click_button(SlowCalculatorPage.BUTTON_8_LOCATOR)
        browser.calculator_page.click_button(SlowCalculatorPage.EQUALS_BUTTON_LOCATOR)

    
    with allure.step("Ожидание отображения результата"):
        browser.calculator_page.wait_until_result_displayed('15')

