import pytest
from selenium import webdriver
from calculator_page import SlowCalculatorPage


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    browser.calculator_page = SlowCalculatorPage(browser)

    browser.calculator_page.set_delay('45')

    browser.calculator_page.click_button(SlowCalculatorPage.BUTTON_7_LOCATOR)
    browser.calculator_page.click_button(SlowCalculatorPage.PLUS_BUTTON_LOCATOR)
    browser.calculator_page.click_button(SlowCalculatorPage.BUTTON_8_LOCATOR)
    browser.calculator_page.click_button(SlowCalculatorPage.EQUALS_BUTTON_LOCATOR)

    browser.calculator_page.wait_until_result_displayed('15')

    browser.quit()
