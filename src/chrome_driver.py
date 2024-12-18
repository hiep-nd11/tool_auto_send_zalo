from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def setup_driver(headless=False):
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    if headless:
        chrome_options.add_argument("--headless")

    # user_data_dir = "/home/nguyen/.config/google-chrome"
    # profile_dir = "Default" 
    # chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
    # chrome_options.add_argument(f"--profile-directory={profile_dir}")
    service = Service("/usr/bin/chromedriver") 
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver