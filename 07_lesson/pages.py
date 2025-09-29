from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def enter_username(self, username):
        wait = WebDriverWait(self.driver, 30)
        user_input = wait.until(EC.visibility_of_element_located((By.ID, 'user-name')))
        user_input.clear()
        user_input.send_keys(username)
    
    def enter_password(self, password):
        wait = WebDriverWait(self.driver, 30)
        password_input = wait.until(EC.visibility_of_element_located((By.ID, 'password')))
        password_input.clear()
        password_input.send_keys(password)
    
    def click_login_button(self):
        wait = WebDriverWait(self.driver, 30)
        login_button = wait.until(EC.element_to_be_clickable((By.ID, 'login-button')))
        login_button.click()

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
    
    def add_product_to_cart(self, product_name):
        wait = WebDriverWait(self.driver, 30)
        add_to_cart_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item_description']//button")))
        add_to_cart_btn.click()
    
    def go_to_cart(self):
        wait = WebDriverWait(self.driver, 30)
        cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'shopping_cart_link')))
        cart_icon.click()

class CartPage:
    def __init__(self, driver):
        self.driver = driver
    
    def checkout(self):
        wait = WebDriverWait(self.driver, 30)
        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, 'checkout')))
        checkout_button.click()

class CheckOutStepOnePage:
    def __init__(self, driver):
        self.driver = driver
    
    def fill_first_name(self, first_name):
        wait = WebDriverWait(self.driver, 30)
        first_name_input = wait.until(EC.visibility_of_element_located((By.ID, 'first-name')))
        first_name_input.clear()
        first_name_input.send_keys(first_name)

    def fill_last_name(self, last_name):
        wait = WebDriverWait(self.driver, 30)
        last_name_input = wait.until(EC.visibility_of_element_located((By.ID, 'last-name')))
        last_name_input.clear()
        last_name_input.send_keys(last_name)
    
    def fill_postal_code(self, postal_code):
        wait = WebDriverWait(self.driver, 30)
        postal_code_input = wait.until(EC.visibility_of_element_located((By.ID, 'postal-code')))
        postal_code_input.clear()
        postal_code_input.send_keys(postal_code)
    
    def continue_checkout(self):
        wait = WebDriverWait(self.driver, 30)
        continue_button = wait.until(EC.element_to_be_clickable((By.ID, 'continue')))
        continue_button.click()

class OverviewPage:
    def __init__(self, driver):
        self.driver = driver
    
    def get_total_amount(self):
        wait = WebDriverWait(self.driver, 30)
        total_amount = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'summary_total_label'))
        ).text
        return float(total_amount.replace('Total: $', ''))
    