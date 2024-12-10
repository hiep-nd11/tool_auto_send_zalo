import time
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from check_login import check_login
from send_message import send_message
from name_distric import get_name_from_district

app = FastAPI()

class MessageData(BaseModel):
    distric_id: Optional[int]
    name: str
    message: str

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
service = Service("/usr/bin/chromedriver")

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://chat.zalo.me/")
# time.sleep(10)

@app.post("/send-message/")
async def send_message_api(data: MessageData):
    try:
        check_login(driver, time.time(), 10)

        distric_id = get_name_from_district(data.distric_id)

        send_message(driver, data.name, data.message, distric_id)
        return {"status": "success", "details": f"Message sent to {data.name}."}

    except HTTPException as e:
        return {"status": "error", "details": e.detail}
    



