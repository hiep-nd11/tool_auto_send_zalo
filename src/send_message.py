import time
from fastapi import FastAPI, HTTPException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def send_message(driver, name, message):
    try:

        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="contact-search-input"]'))
        )
        search_box.click()
        search_box.clear()
        search_box.send_keys(name)

        contact = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="gridv2 conv-item conv-rel   lv-1 fluid tiny grid-fluid-8"]'))
        )
        contact.click()

        message_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@id="input_line_0"]'))
        )
        message_box.click()
        message_box.send_keys(message)
        
        send_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//i[@class="fa fa-Sent-msg_24_Line pre"]'))
        )
        send_button.click()
        driver.find_element(By.XPATH, '//input[@id="contact-search-input"]').click()

        # driver.find_element(By.XPATH, '//input[@id="contact-search-input"]').send_keys("cloud")
        # time.sleep(5)
        # driver.find_element(By.XPATH, '//div[@id="friend-item-4473111165018993534"]').click()
        # time.sleep(2)
        # driver.find_element(By.XPATH, '//div[@id="input_line_0"]').click()
        # time.sleep(2)
        # driver.find_element(By.XPATH, '//div[@id="input_line_0"]').send_keys("aaaaaaaaabbbbbbbbbbbb")
        # time.sleep(2)
        # driver.find_element(By.XPATH, '//i[@class="fa fa-Sent-msg_24_Line pre"]').click()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send message: {str(e)}")