from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver
    
    DELAY_INPUT_LOCATOR = (By.ID, 'delay')
    RESULT_FIELD_LOCATOR = (By.CLASS_NAME, 'screen')
    BUTTON_7_LOCATOR = (By.XPATH, "//span[contains(text(), '7')]")
    PLUS_BUTTON_LOCATOR = (By.XPATH, "//span[contains(text(), '+')]")
    BUTTON_8_LOCATOR = (By.XPATH, "//span[contains(text(), '8')]")
    EQUALS_BUTTON_LOCATOR = (By.XPATH, "//span[contains(text(), '=')]")

    def set_delay(self, delay_value):
        input_field = self.driver.find_element(*self.DELAY_INPUT_LOCATOR)
        input_field.clear()
        input_field.send_keys(delay_value)

    def click_button(self, button_locator):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        )
        button.click()

    def wait_until_result_displayed(self, result_text):
        WebDriverWait(self.driver, timeout=60).until(
            EC.text_to_be_present_in_element(self.RESULT_FIELD_LOCATOR, result_text)
        )
        