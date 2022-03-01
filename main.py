# LBSBTFR

import time
import argparse

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from commands.login_by_qr import LoginByQR
from commands.send_numbers_chunks import SendNumbersByChunks

LINK_TO_TELEGRAM = "https://web.telegram.org/z/"
LINK = "https://web.telegram.org/z/#?tgaddr=tg%3A%2F%2Fresolve%3Fdomain%3D{0}"

drivers = [webdriver.Chrome, webdriver.Ie, webdriver.Edge, webdriver.Opera, webdriver.Safari, webdriver.Firefox]
# path_to_numbers = r"F:\LBSFTFR\callfriend\numbers.txt"


if __name__ == '__main__':
    # Get path to numbers
    parser = argparse.ArgumentParser(description='Pass to numbers')
    parser.add_argument('--path_to_numbers', help='path to numbers in format +7ххххххххххх та +375ххххххххх')
    args = parser.parse_args()

    path_to_numbers = args.path_to_numbers

    if path_to_numbers is None:
        print("--path_to_numbers should be added")
        quit()

    # Run driver from existed.
    driver = None
    for driver_func in drivers:
        try:
            driver = driver_func()
            break
        except:
            print("driver not found")
    else:
        print("Drivers for browasers not found")
        quit()

    login_qr = LoginByQR(driver, LINK.format("DzvinokDruguBot"))
    login_qr.wait_user_read_qr()
    login_qr.wait_bot_opened()

    # TODO:
    # if bot not started earlier, or should be restarted than click on "Start bot" or "Restart bot"

    chunks_numbers_obj = SendNumbersByChunks(path_to_numbers)

    for line in chunks_numbers_obj.text_numbers:
        time.sleep(1)
        element = driver.find_element_by_id("editable-message-text")
        element.send_keys(line)
        element.send_keys(Keys.RETURN)
