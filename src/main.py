import time
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException


from check_login import check_login
from send_message import send_message
from chrome_driver import setup_driver
from name_distric import get_name_from_district

app = FastAPI()

class MessageData(BaseModel):
    distric_id: Optional[int]
    name: str
    message: str

driver = setup_driver(headless=False)
driver.get("https://chat.zalo.me/")

@app.post("/send-message/")
async def send_message_api(data: MessageData):
    try:
        check_login(driver, time.time(), 10)

        distric_id = get_name_from_district(data.distric_id)

        send_message(driver, data.name, data.message, distric_id)
        return {"status": "success", "details": f"Message sent to {data.name}."}

    except HTTPException as e:
        return {"status": "error", "details": e.detail}
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


