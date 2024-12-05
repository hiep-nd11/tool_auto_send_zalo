import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from check_login import check_login, check_login2

max_wait_time = 180  
start_time = time.time() 

chrome_options = Options()

service = Service("/usr/bin/chromedriver")  # Kiểm tra đường dẫn với `which chromedriver`

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Mở trình duyệt toàn màn hình
options.add_argument("--disable-notifications")  # Tắt thông báo
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://chat.zalo.me/")


check_login2(driver, start_time, max_wait_time)