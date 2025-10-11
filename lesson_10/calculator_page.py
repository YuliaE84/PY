from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    """
    Класс описывает интерфейс взаимодействия с калькулятором на странице.
    Включает основные методы для установки задержки,
    нажатия кнопок и ожидания результата вычислений.
    """
    def __init__(self, driver):
        """
        Инициализирует объект класса.

        :param driver: Экземпляр Selenium WebDriver.
        """
        self.driver = driver

    # Локаторы элементов интерфейса
    DELAY_INPUT_LOCATOR = (By.ID, 'delay')
    RESULT_FIELD_LOCATOR = (By.CLASS_NAME, 'screen')
    BUTTON_7_LOCATOR = (By.XPATH, "//span[contains(text(), '7')]")
    PLUS_BUTTON_LOCATOR = (By.XPATH, "//span[contains(text(), '+')]")
    BUTTON_8_LOCATOR = (By.XPATH, "//span[contains(text(), '8')]")
    EQUALS_BUTTON_LOCATOR = (By.XPATH, "//span[contains(text(), '=')]")

    def set_delay(self, delay_value):
        """
        Устанавливает временную задержку на выполнение операций калькулятора.
        """
        
        input_field = self.driver.find_element(*self.DELAY_INPUT_LOCATOR)
        input_field.clear()
        input_field.send_keys(delay_value)

    def click_button(self, button_locator):
        """
        Производит клик по указанной кнопке на калькуляторе.
        """
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        )
        button.click()

    def wait_until_result_displayed(self, result_text):
        """
        Ожидает отображения указанного результата в окне калькулятора.

        :param result_text: Текст результата, который ожидается увидеть.
        """
        WebDriverWait(self.driver, timeout=60).until(
            EC.text_to_be_present_in_element(self.RESULT_FIELD_LOCATOR, result_text)
        )
