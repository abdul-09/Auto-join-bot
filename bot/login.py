# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# def automated_login(driver, email, password):
#     driver.get("https://www.linkedin.com/login")
    
#     # Wait for login form to load
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
    
#     # Fill in the form using Selenium's send_keys instead of JavaScript
#     email_field = driver.find_element(By.ID, "username")
#     email_field.clear()
#     email_field.send_keys(email)
    
#     password_field = driver.find_element(By.ID, "password")
#     password_field.clear()
#     password_field.send_keys(password)
    
#     # Wait for button to be clickable
#     sign_in_button = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
#     )
    
#     # Scroll into view and click using JavaScript if normal click doesn't work
#     driver.execute_script("arguments[0].scrollIntoView();", sign_in_button)
#     time.sleep(1)
#     driver.execute_script("arguments[0].click();", sign_in_button)
    
#     print("✅ Sign in button clicked. Waiting for redirect...")
    
#     # Wait for redirect to complete (check for home feed element)
#     try:
#         WebDriverWait(driver, 30).until(
#             EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'scaffold-finite-scroll')]"))
#         )
#         print("✔ Login successful - redirected to home page")
#     except:
#         print("❌ Login may have failed - check for error messages")
    
#     time.sleep(3)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def automated_login(driver, email, password):
    driver.get("https://www.linkedin.com/login")

    # Wait for the login form to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

    # Set email and password via JavaScript
    driver.execute_script(f"document.getElementById('username').value = '{email}';")
    driver.execute_script(f"document.getElementById('password').value = '{password}';")

    # Dispatch 'input' events to trigger LinkedIn's validation
    driver.execute_script("""
        const event = new Event('input', { bubbles: true });
        document.getElementById('username').dispatchEvent(event);
        document.getElementById('password').dispatchEvent(event);
    """)

    time.sleep(1)  # Allow time for LinkedIn to process the input

    # Click the "Sign in" button using JavaScript
    driver.execute_script("document.querySelector('button[type=submit]').click();")

    print("✅ Sign in button clicked. Waiting for redirect...")
    time.sleep(3)

    
   
    
    # Wait for either success or failure
    try:
        WebDriverWait(driver, 60).until(
            lambda d: "feed" in d.current_url.lower() or "login" in d.current_url.lower()
        )
        
        if "login" in driver.current_url.lower():
            print("❌ Login may have failed - check page for error messages")
            return False
        else:
            print("✔ Login successful")
            return True
            
    except Exception as e:
        print(f"⚠ Unexpected state: {str(e)}")
        return False