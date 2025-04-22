def manual_login(driver):
    driver.get("https://www.linkedin.com/login")

    # Hide webdriver property (extra stealth for some versions)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    print("Please log in manually. Press Enter when done.")
    input()