from utils import *
from selenium import webdriver
from selenium.webdriver.common.by import By

log = logger()
scraper_logger = log.logger("main","main.log")

url = "https://meet.google.com/nhz-qfpu-sow"
driver = webdriver.Chrome()
driver.get(url)
xpath_selector = "//span[text()='Return to home screen']"
is_clicked = click_element(driver, xpath_selector, By.XPATH, scraper_logger)
if is_clicked:
    emailSendObj = EmailSend(receiver_mails)
    name = 'Main Logs'
    subject = f"Report: {name}"
    emailSendObj.send_email(subject, f"Element One Clicked Successfully at: {url}")
    del emailSendObj
    scraper_logger.info(f"Element One Clicked Successfully at: {url}")

url = "https://google.com/nhz-qfpu-sow"
driver.get(url)
xpath_selector = "//span[text()='Return to home screen']"
is_clicked = click_element(driver, xpath_selector, By.XPATH, scraper_logger)
if is_clicked:
    emailSendObj = EmailSend(receiver_mails)
    name = 'Main Logs'
    subject = f"Report: {name}"
    emailSendObj.send_email(subject, f"Element Two Clicked Successfully at: {url}")
    del emailSendObj
    scraper_logger.info(f"Element Two Clicked Successfully at: {url}")

driver.quit()