from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OverviewPage:
    def __init__(self, driver):
        self.driver = driver
    
    def get_total_amount(self):
        total_amount = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'summary_total_label'))
        ).text
        return float(total_amount.replace('Total: $', ''))
    