import time
from selenium.common.exceptions import NoSuchElementException


class LoginByQR:
    SLEEP_SECONDS = 3
    CONTAINER_MENU_NAME = "ripple-container"

    def __init__(self, driver, page_to_login):
        """Login by QR"""
        self.driver = driver
        self.page_to_login = page_to_login
        self.driver.get(page_to_login)

    def wait_user_read_qr(self):
        while True:
            time.sleep(LoginByQR.SLEEP_SECONDS)
            try:
                element = self.driver.find_element_by_class_name(LoginByQR.CONTAINER_MENU_NAME)
                if element is not None:
                    break
            except NoSuchElementException as exept:
                print("NOT")

        print("FOUND")

    def wait_bot_opened(self):
        while True:
            time.sleep(LoginByQR.SLEEP_SECONDS)
            element = element2 = None
            try:
                element = self.driver.find_element_by_id("editable-message-text")
            except NoSuchElementException as exept:
                print("Bot not found yet. Please, wait")

            element2 = "Restart bot" in self.driver.page_source or "Start bot" in self.driver.page_source
            if element is not None or element2 is not None:
                break
        print("Bot Found")