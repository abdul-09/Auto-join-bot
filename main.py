from bot.driver_setup import create_driver
from bot.login import manual_login
from bot.navigator import scroll_to_load
from bot.button_clicker import find_and_click_buttons
from bot.logger import log_session

def main():
    driver = create_driver()
    
    try:
        manual_login(driver)
        driver.get("https://www.linkedin.com/groups/discover/")
        scroll_to_load(driver, scrolls=10)
        click_count = find_and_click_buttons(driver)
        log_session(click_count)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()