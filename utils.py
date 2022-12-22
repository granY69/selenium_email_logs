from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from logs import logger
from email_send import EmailSend

receiver_mails = ["cbyamin806@gmail.com"]

def find_element(driver: webdriver, selector: str, selector_type, logger: logger, timeout=3):
    try:
        element_present = EC.presence_of_element_located(
            (selector_type, selector))
        element = WebDriverWait(driver, timeout).until(element_present)
        return element
    except TimeoutException:
        if logger:
            logger.error(f"Selector: {selector}. Element Not Found")
        # print(f"Selector: {selector}. Element Not Found")
        return None

def click_element(driver: webdriver, selector: str, selector_type, logger: logger, timeout=10):
    element = find_element(driver, selector, selector_type, logger, timeout)
    if element:
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        return True
    else:
        if logger:
            logger.error(
                f"Element Not Found. Click Element Not Performed at {selector}.")
        # print(f"Element Not Found. Click Element Not Performed at {selector}.")
        return None
