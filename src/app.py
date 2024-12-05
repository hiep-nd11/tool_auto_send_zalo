import time
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from check_login import check_login
from send_message import send_message

# FastAPI app
app = FastAPI()

# Pydantic model for input validation
class MessageData(BaseModel):
    type: str
    name: str
    message: str

# Selenium setup (global driver)
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
service = Service("/usr/bin/chromedriver")

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://chat.zalo.me/")

# API endpoint
@app.post("/send-message/")
async def send_message_api(data: MessageData):
    try:
        # Check login
        check_login(driver, time.time(), 180)
        
        # Send message
        send_message(driver, data.name, data.message)
        return {"status": "success", "details": f"Message sent to {data.name}."}

    except HTTPException as e:
        return {"status": "error", "details": e.detail}


# max_wait_time = 180  
# start_time = time.time() 

# chrome_options = Options()

# service = Service("/usr/bin/chromedriver")  

# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")  
# options.add_argument("--disable-notifications")  
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# driver = webdriver.Chrome(service=service, options=options)
# driver.get("https://chat.zalo.me/")


# check_login(driver, start_time, max_wait_time)
# time.sleep(3)

# driver.find_element(By.XPATH, '//input[@id="contact-search-input"]').click()

# driver.find_element(By.XPATH, '//input[@id="contact-search-input"]').send_keys("cloud")
# time.sleep(5)
# driver.find_element(By.XPATH, '//div[@id="friend-item-4473111165018993534"]').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//div[@id="input_line_0"]').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//div[@id="input_line_0"]').send_keys("aaaaaaaaabbbbbbbbbbbb")
# time.sleep(2)
# driver.find_element(By.XPATH, '//i[@class="fa fa-Sent-msg_24_Line pre"]').click()
# time.sleep(5000)


