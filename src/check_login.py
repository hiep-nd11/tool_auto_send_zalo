import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def check_login(driver, start_time, max_wait_time):
    while True:
        try:
            driver.find_element(By.XPATH, '//div[@class="group-search grid-item"]')
            print("Đăng nhập thành công!")
            break  

        except NoSuchElementException:
            print("Chưa đăng nhập, vui lòng đăng nhập...")

            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//div[@class="group-search grid-item"]'))
                )

            except TimeoutException:
                pass  

        finally:
            if time.time() - start_time > max_wait_time:
                print("Hết thời gian chờ! Bạn chưa đăng nhập.")
                break

# def check_login(driver):
#     try:
#         wait = WebDriverWait(driver, 10)
#         check_search = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="group-search grid-item"]')))
#         return True
#     except TimeoutException:
#         return False
    
    
#     # try:
#     #     driver.find_element(By.XPATH, '//div[@class="group-search grid-item"]')
#     #     return True
#     # except NoSuchElementException:
#     #     return False