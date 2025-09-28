class CartPage:
    def __init__(self, driver):
        self.driver = driver
    
    def checkout(self):
        checkout_button = self.driver.find_element(By.ID, 'checkout')
        checkout_button.click()
        