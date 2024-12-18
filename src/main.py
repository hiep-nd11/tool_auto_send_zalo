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
    distric_id: Optional[str]
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
    uvicorn.run(app, host="localhost", port=8000)

# import time
# from typing import Optional
# from pydantic import BaseModel
# from fastapi import FastAPI, WebSocket, WebSocketDisconnect
# from fastapi.responses import HTMLResponse

# from check_login import check_login
# from send_message import send_message
# from chrome_driver import setup_driver
# from name_distric import get_name_from_district

# app = FastAPI()

# class MessageData(BaseModel):
#     distric_id: Optional[int]
#     name: str
#     message: str

# driver = setup_driver(headless=False)
# driver.get("https://chat.zalo.me/")

# connected_clients = []  

# @app.websocket("/ws/")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     connected_clients.append(websocket)
#     try:
#         while True:
#             data = await websocket.receive_json()
#             message_data = MessageData(**data)
#             try:
#                 check_login(driver, time.time(), 10)
#                 distric_id = get_name_from_district(message_data.distric_id)
#                 send_message(driver, message_data.name, message_data.message, distric_id)
#                 await websocket.send_json({"status": "success", "details": f"Message sent to {message_data.name}."})
#             except Exception as e:
#                 await websocket.send_json({"status": "error", "details": str(e)})
#     except WebSocketDisconnect:
#         connected_clients.remove(websocket)

# @app.get("/")
# async def get():

#     return HTMLResponse("""
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>WebSocket Test</title>
#     </head>
#     <body>
#         <h1>WebSocket Client</h1>
#         <form id="sendMessage">
#             <label for="message">Message:</label>
#             <input id="message" type="text" />
#             <button>Send</button>
#         </form>
#         <ul id="messages"></ul>
#         <script>
#             const ws = new WebSocket("ws://localhost:8000/ws/");
#             ws.onmessage = event => {
#                 const messages = document.getElementById("messages");
#                 const message = document.createElement("li");
#                 message.textContent = event.data;
#                 messages.appendChild(message);
#             };
#             document.getElementById("sendMessage").onsubmit = event => {
#                 event.preventDefault();
#                 const input = document.getElementById("message");
#                 ws.send(input.value);
#                 input.value = "";
#             };
#         </script>
#     </body>
#     </html>
#     """)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)


