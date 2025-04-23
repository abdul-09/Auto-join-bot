import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def automated_login(driver, email, password):
    driver.get("https://www.linkedin.com/login")

    # Find and fill email
    email_input = driver.find_element(By.ID, "username")
    email_input.clear()
    email_input.send_keys(email)
    time.sleep(1)

    # Find and fill password
    password_input = driver.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys(password)
    time.sleep(1)

    # Submit login
    password_input.send_keys(Keys.RETURN)

    print("Logged in automatically.")
    time.sleep(3)  # Wait for redirect to finish
