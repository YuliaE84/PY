class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        
    def add_product_to_cart(self, product_name):
        add_to_cart_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item_description']//button"))
        )
        add_to_cart_btn.click()
    
    def go_to_cart(self):
        cart_icon = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
        cart_icon.click()
        