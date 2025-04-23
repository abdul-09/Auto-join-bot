from selenium.webdriver.common.by import By
import time
import random
from config import TARGET_KEYWORDS, MAX_CLICKS

def find_and_click_buttons(driver):
    buttons = driver.find_elements(By.XPATH, "//button")
    clicked = 0

    for btn in buttons:
        try:
            text = btn.text.strip()
            if any(k.lower() in text.lower() for k in TARGET_KEYWORDS):
                # Scroll button into view to avoid intercept errors
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", btn)
                time.sleep(random.uniform(1, 2))

                btn.click()
                print(f"Clicked: {text}")
                clicked += 1
                time.sleep(random.uniform(1.5, 3.5))
                if clicked >= MAX_CLICKS:
                    break
        except Exception as e:
            print(f"Skipping a button due to error: {e}")
    return clicked

def connect_people(driver):

    buttons = driver.find_elements(By.XPATH, "//button")
    clicked = 0

    for btn in buttons:
        try:
            label = btn.text.strip()
            if "Connect" in label and btn.is_displayed():
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", btn)
                time.sleep(random.uniform(1, 2))
                btn.click()
                print(f"Clicked Connect for: {label}")
                clicked += 1
                time.sleep(random.uniform(1.5, 3.5))
                if clicked >= MAX_CLICKS:
                    break
        except Exception as e:
            print(f"Error clicking connect: {e}")

    return clicked

def follow_people(driver):

    buttons = driver.find_elements(By.XPATH, "//button")
    clicked = 0

    for btn in buttons:
        try:
            label = btn.text.strip()
            if "Follow" in label and btn.is_displayed():
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", btn)
                time.sleep(random.uniform(1, 2))
                btn.click()
                print(f"Clicked Follow for: {label}")
                clicked += 1
                time.sleep(random.uniform(1.5, 3.5))
                if clicked >= MAX_CLICKS:
                    break
        except Exception as e:
            print(f"Error clicking follow: {e}")

    return clicked
