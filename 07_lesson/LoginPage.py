from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def enter_username(self, username):
        wait = WebDriverWait(self.driver, 10)
        user_input = wait.until(EC.visibility_of_element_located((By.ID, 'user-name')))
        user_input.clear()
        user_input.send_keys(username)
    
    def enter_password(self, password):
        wait = WebDriverWait(self.driver, 10)
        password_input = wait.until(EC.visibility_of_element_located((By.ID, 'password')))
        password_input.clear()
        password_input.send_keys(password)
    
    def click_login_button(self):
        wait = WebDriverWait(self.driver, 10)
        login_button = wait.until(EC.element_to_be_clickable((By.ID, 'login-button')))
        login_button.click()
        