import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=options)
    yield driver
    driver.quit()
def test_fill_and_submit_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 40)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    first_name_field = wait.until(EC.presence_of_element_located((By.NAME, "first-name")))
    first_name_field.send_keys("Иван")
    last_name_field = wait.until(EC.presence_of_element_located((By.NAME, "last-name")))
    last_name_field.send_keys("Петров")
    address_field = wait.until(EC.presence_of_element_located((By.NAME, "address")))
    address_field.send_keys("Ленина, 55-3")
    email_field = wait.until(EC.presence_of_element_located((By.NAME, "e-mail")))
    email_field.send_keys("test@skypro.com")
    phone_field = wait.until(EC.presence_of_element_located((By.NAME, "phone")))
    phone_field.send_keys("+7985899998787")
    zip_code_field = wait.until(EC.presence_of_element_located((By.NAME, "zip-code")))
    zip_code_field.clear()
    city_field = wait.until(EC.presence_of_element_located((By.NAME, "city")))
    city_field.send_keys("Москва")
    country_field = wait.until(EC.presence_of_element_located((By.NAME, "country")))
    country_field.send_keys("Россия")
    job_position_field = wait.until(EC.presence_of_element_located((By.NAME, "job-position")))
    job_position_field.send_keys("QA")
    company_field = wait.until(EC.presence_of_element_located((By.NAME, "company")))
    company_field.send_keys("SkyPro")

    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()

    zip_code_field_after_submit = wait.until(EC.presence_of_element_located((By.NAME, "zip-code")))
    assert "is-invalid" in zip_code_field_after_submit.get_attribute("class")

    valid_fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
    for field_name in valid_fields:
        field = wait.until(EC.presence_of_element_located((By.NAME, field_name)))
        assert "is-valid" in field.get_attribute("class")
        

