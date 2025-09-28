class CheckOutStepOnePage:
    def __init__(self, driver):
        self.driver = driver
    
    def fill_first_name(self, first_name):
        first_name_input = self.driver.find_element(By.ID, 'first-name')
        first_name_input.clear()
        first_name_input.send_keys(first_name)
    
    def fill_last_name(self, last_name):
        last_name_input = self.driver.find_element(By.ID, 'last-name')
        last_name_input.clear()
        last_name_input.send_keys(last_name)
    
    def fill_postal_code(self, postal_code):
        postal_code_input = self.driver.find_element(By.ID, 'postal-code')
        postal_code_input.clear()
        postal_code_input.send_keys(postal_code)
    
    def continue_checkout(self):
        continue_button = self.driver.find_element(By.ID, 'continue')
        continue_button.click()
        