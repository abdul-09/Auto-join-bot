import undetected_chromedriver as uc

def create_driver():
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    return uc.Chrome(options=options)