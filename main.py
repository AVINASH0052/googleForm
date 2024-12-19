from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to ChromeDriver
webdriver_path = "/Users/avinash/Downloads/chromedriver-mac-arm64/chromedriver"

# Google Form URL
form_url = "https://forms.gle/WT68aV5UnPajeoSc8"

# Data to fill in the form
form_data = {
    "full_name": "Avinash Vikram Singh",
    "contact_number": "7052985015",
    "email": "avinashvs0052@gmail.com",
    "address": "Laxmi Nagar, New Delhi",
    "pin_code": "110092",
    "dob": "2003-08-05",  # Input format for type="date" should be yyyy-MM-dd
    "gender": "Male",
    "verification_code": "GNFPYC"
}

# Open the browser
driver_service = Service(webdriver_path)
driver = webdriver.Chrome(service=driver_service)
driver.get(form_url)
wait = WebDriverWait(driver, 20)  # Explicit wait for elements to load

try:
    # Helper function to fill a field
    def scroll_and_fill(locator, value):
        element = wait.until(EC.presence_of_element_located(locator))
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        wait.until(EC.element_to_be_clickable(locator))
        element.send_keys(value)

    # Fill out the form fields with updated locators
    scroll_and_fill((By.XPATH, "//input[@aria-labelledby='i1 i4']"), form_data["full_name"])  # Full Name
    scroll_and_fill((By.XPATH, "//input[@aria-labelledby='i6 i9']"), form_data["contact_number"])  # Contact Number
    scroll_and_fill((By.XPATH, "//input[@aria-labelledby='i11 i14']"), form_data["email"])  # Email ID
    scroll_and_fill((By.XPATH, "//textarea[@aria-labelledby='i16 i19']"), form_data["address"])  # Full Address
    scroll_and_fill((By.XPATH, "//input[@aria-labelledby='i21 i24']"), form_data["pin_code"])  # Pin Code
    scroll_and_fill((By.XPATH, "//input[@aria-labelledby='i31']"), form_data["dob"])  # Date of Birth
    scroll_and_fill((By.XPATH, "//input[@aria-labelledby='i32 i35']"), form_data["gender"])  # Gender
    scroll_and_fill((By.XPATH, "//input[@aria-labelledby='i37 i40']"), form_data["verification_code"])  # Verification Code

    # Submit the form
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Submit']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

    time.sleep(2)  # Wait for submission to complete
finally:
    # Close the browser
    driver.quit()
