# from bot.driver_setup import create_driver
# from bot.login import automated_login
# from bot.navigator import scroll_to_load
# from bot.button_clicker import find_and_click_buttons
# from bot.logger import log_session
# from getpass import getpass

# def main():
#     driver = create_driver()
    
#     try:
#         email = input("Enter your LinkedIn email: ")
#         password = getpass("Enter your LinkedIn password: ")  # safely hides password input

#         automated_login(driver, email, password)
#         driver.execute_script("console.log('webdriver:', navigator.webdriver);")
#         driver.get("https://www.linkedin.com/groups/discover/")
#         scroll_to_load(driver, scrolls=10)
#         click_count = find_and_click_buttons(driver)
#         log_session(click_count)
#     finally:
#         driver.quit()


# if __name__ == "__main__":
#     main()
from bot.driver_setup import create_driver
from bot.login import automated_login
from bot.navigator import scroll_to_load
from bot.button_clicker import find_and_click_buttons, connect_people, follow_people
from bot.logger import log_session
from getpass import getpass

def main():
    driver = create_driver()
    try:
        # Prompt for credentials
        email = input("Enter your LinkedIn email: ")
        password = getpass("Enter your LinkedIn password: ")

        # Log in
        automated_login(driver, email, password)

        # Choose operation mode
        mode = input("Mode? (groups/connect/follow): ").strip().lower()

        if mode == "groups":
            print("[MODE] Joining LinkedIn Groups...")
            driver.get("https://www.linkedin.com/groups/discover/")
            scroll_to_load(driver, scrolls=10)
            click_count = find_and_click_buttons(driver)
            log_session("groups", click_count)

        elif mode == "connect":
            print("[MODE] Connecting to People...")
            driver.get("https://www.linkedin.com/mynetwork/")
            scroll_to_load(driver, scrolls=10)
            click_count = connect_people(driver)
            log_session("connect", click_count)

        elif mode == "follow":
            print("[MODE] Following People...")
            driver.get("https://www.linkedin.com/feed/follow/")
            scroll_to_load(driver, scrolls=10)
            click_count = follow_people(driver)
            log_session("follow", click_count)

    except Exception as e:
        print(f"⚠️ Error occurred: {e}")

    finally:
        try:
            driver.quit()
        except Exception as e:
            print(f"⚠️ Failed to quit browser cleanly: {e}")

if __name__ == "__main__":
    main()
