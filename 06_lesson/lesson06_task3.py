from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = FirefoxService(executable_path=r'D:\загрузки\geckodriver-v0.35.0-win64\geckodriver.exe')

driver = webdriver.Firefox(service=service)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

third_image = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, "(//img)[3]"))
)

image_src = third_image.get_attribute("src")
print(image_src)

driver.quit()
