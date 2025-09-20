from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = FirefoxService(executable_path=r'D:\загрузки\geckodriver-v0.35.0-win64\geckodriver.exe')

driver = webdriver.Firefox(service=service)

driver.get("http://uitestingplayground.com/ajax")

button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
button.click()

green_block = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
    )

text_from_green_block = green_block.text.strip()
print(text_from_green_block)

driver.quit()
