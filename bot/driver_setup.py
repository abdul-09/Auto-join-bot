import undetected_chromedriver as uc

def create_driver():
    options = uc.ChromeOptions()
    
    # Start like a normal user would
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    # # Spoof common headers
    # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
    #                      "AppleWebKit/537.36 (KHTML, like Gecko) " +
    #                      "Chrome/135.0.7049.96 Safari/537.36")

    # # Optional: set realistic window size
    # options.add_argument("window-size=1920,1080")

    # Optional: load with extensions disabled
    options.add_argument("--disable-extensions")

    # Optional: language
    options.add_argument("--lang=en-US")

    driver = uc.Chrome(options=options, use_subprocess=True)


    return driver
