import sys
import os
import random
from selenium import webdriver
import requests
import time
from selenium.common.exceptions import WebDriverException, TimeoutException

splash = """

 Built for Educational and testing Purposes only
 Built By [Bichitra-Linux]

 support the Project on:
 https://github.com/bichitra-linux
"""

print(splash)
time.sleep(10)

def request(target_url, timeo, stay_time, browser_type):
    try:
        if browser_type == 'chrome':
            driver = webdriver.Chrome()
        elif browser_type == 'firefox':
            driver = webdriver.Firefox()
        elif browser_type == 'edge':
            driver = webdriver.Edge()
        elif browser_type == 'safari':
            driver = webdriver.Safari()
        else:
            print("Unsupported browser type")
            return

        driver.set_page_load_timeout(timeo)
        driver.get(target_url)
        time.sleep(stay_time)
    except TimeoutException:
        print("Error: Page load timed out")
    except WebDriverException as e:
        print(f"WebDriver error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        driver.quit()

def get_valid_input(prompt, input_type):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

target = input("\033[1;33;40mEnter The Target Website URL: ").strip()
timeout = get_valid_input("\033[1;33;40mEnter The Time Out (In Seconds): ", int)
stay = get_valid_input("\033[1;33;40mEnter The Stay Time (In Seconds): ", int)
browser = input("\033[1;33;40mEnter The Browser Type (chrome/firefox/edge/safari): ").strip().lower()

while True:
    request(target, timeout, stay, browser)
    print("\033[1;32;40mSleeping For 5 Seconds")
    time.sleep(5)