import unittest
from selenium import webdriver
from calculator_page import SlowCalculatorPage


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.calculator_page = SlowCalculatorPage(self.driver)

    def test_addition_with_delay(self):
        self.calculator_page.set_delay('45')
        
        self.calculator_page.click_button(SlowCalculatorPage.BUTTON_7_LOCATOR)
        self.calculator_page.click_button(SlowCalculatorPage.PLUS_BUTTON_LOCATOR)
        self.calculator_page.click_button(SlowCalculatorPage.BUTTON_8_LOCATOR)
        self.calculator_page.click_button(SlowCalculatorPage.EQUALS_BUTTON_LOCATOR)
        
        self.calculator_page.wait_until_result_displayed('15')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
